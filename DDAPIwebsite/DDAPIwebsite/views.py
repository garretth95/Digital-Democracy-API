# core functionality of API
# created by Garrett Heald

import json
import time
import os
import re
from _datetime import datetime
from datetime import timedelta, datetime
from django.db.models import F
from django.utils import timezone

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from itsdangerous import URLSafeSerializer

from .forms import UserForm
from .models import User, UserGroup
from .queryDB import get_json_from_backend

from .call import parse_api_calls, replace_variables

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
api_file = os.path.join(THIS_FOLDER, 'sampleAPIcalls.txt')

# not currently used
billTypeDict = ['A', 'AB', 'ABX1', 'ABX2', 'ACA', 'ACR', 'ACRX2', 'AJR', 'B', 'BUD', 'C', 'E', 'HB', 'HCR', 'HJR',
                'HM', 'HR', 'J', 'K', 'L', 'NON', 'R', 'S', 'SB', 'SBX1', 'SBX2', 'SCA', 'SCAX1', 'SCR', 'SCRX1',
                'SCRX2', 'SJR', 'SM', 'SPB', 'SR', 'SRX1', 'SRX2']

# get API calls from text file using call.py
api_calls = parse_api_calls(api_file)


def index(request):
    return render(request, 'index.html')


def request_access(request):
    return render(request, "request_access.html")


# view for adding new user to user database
def new_user(request):
    # form submission, if GET then probably a refresh -> will redirect
    if request.method == 'POST':

        form = UserForm(request.POST)

        # if the form submitted is valid
        if form.is_valid():
            user_dict = form.cleaned_data

            s = URLSafeSerializer(user_dict.get('email'))
            key = s.dumps(str(int(time.time() * 100)))

            group = UserGroup.objects.get(pk=1)  # default set to 1, as base user group

            user = User(first_name=user_dict.get('first_name'), last_name=user_dict.get('last_name'),
                        email=user_dict.get('email'), key=key, user_group=group)

            # don't add user to the db if they already exist
            if not User.objects.filter(email=user.email).exists():

                user.save()
                return render(request, 'new_user.html', {'user': user})

            else:
                email_error = 'User with the email "' + user.email + '" already exists'
                return render(request, 'request_access.html', {'email_error': email_error})

        else:
            return render(request, 'request_access.html', {'form': form})

    return HttpResponseRedirect('/request_access/')


# helper function for authenticating user
def check_api_key(email, key):  # checks User DB to see if email exists and key matches email

    if User.objects.filter(email=email).exists() and User.objects.get(email=email).key == key:
        return True
    else:
        return False


# Don't really use
def no_access(request):
    return render(request, 'no_access.html')


# Throttling and Metering check help function
def meter_throttle_check(user):

    if user.latest_request is None:  # new user
        User.objects.filter(pk=user.id).update(latest_request=timezone.now())

        # increment day request count
        User.objects.filter(pk=user.id).update(day_request_count=F('day_request_count') + 1)

        # increment minute request count
        User.objects.filter(pk=user.id).update(minute_request_count=F('minute_request_count') + 1)

    else:  # not new user

        if (timezone.now() - user.latest_request).seconds <= 60:  # within 1 minute

            if user.minute_request_count >= user.user_group.throttling_rate:
                return False

            # increment minute request count
            User.objects.filter(pk=user.id).update(minute_request_count=F('minute_request_count') + 1)

        else:   # longer than 1 minute
            # reset minute request count (throttling)
            User.objects.filter(pk=user.id).update(minute_request_count=1)
            User.objects.filter(pk=user.id).update(latest_request=timezone.now())

        if (timezone.now() - user.latest_request).days == 0:  # within 1 day

            if user.day_request_count >= user.user_group.metering_rate:
                return False

            # increment day request count
            User.objects.filter(pk=user.id).update(day_request_count=F('day_request_count') + 1)

        else:   # longer than 1 day
            # reset day request count (metering)
            User.objects.filter(pk=user.id).update(day_request_count=1)
            User.objects.filter(pk=user.id).update(latest_request=timezone.now())

    return True


# main API view logic
def service(request):

    if request.method == 'GET':

        if 'HTTP_EMAIL' in request.META and 'HTTP_API_KEY' in request.META \
                and check_api_key(request.META.get('HTTP_EMAIL'), request.META.get('HTTP_API_KEY')):

            # here is where we check throttling and metering values

            if meter_throttle_check(User.objects.get(email=request.META.get('HTTP_EMAIL'))):

                param_list = request.GET.dict()

                if len(param_list) > 0:

                    callType = param_list.pop('callType', '')

                    if len(callType) == 0:  # no call type parameter
                        return HttpResponse('Error 400: callType parameter is required to make a request.', status=400)

                    if callType not in api_calls:  # we don't support this call type
                        return HttpResponse('Error 400: "' + callType + '" is not a valid callType.', status=400)
                    else:
                        avail_params = api_calls[callType].get('params')  # get the parameters from the callType
                        avail_param_names = []
                        param_list_names = []
                        for param, val in avail_params.items():  # get list of names of parameters according to callType
                            avail_param_names.append(param)
                        for param, val in param_list.items():  # get list of names of parameters provided in request
                            param_list_names.append(param)

                        # incorrect amount of parameters or incorrect parameters
                        if len(avail_param_names) != len(param_list_names) or \
                                sorted(list(set(avail_param_names) & set(param_list_names))) != sorted(avail_param_names):

                            return HttpResponse('Error 400: ' + callType + ' require params: ' +
                                                ' '.join(avail_param_names), status=400)

                        else:   # PARAMETERS ARE CORRECT!!

                            # this is where error checking for types will be

                            type_check = True
                            for param, val in param_list.items():

                                # need to check if datetime type

                                if avail_params[param] == 'String' and not isinstance(val, str):  # redundant
                                    type_check = False
                                if avail_params[param] == 'Integer':
                                    try:
                                        int(val)
                                    except ValueError:
                                        type_check = False
                                if avail_params[param] == 'Date':
                                    try:
                                        datetime.datetime.strptime(val, '%Y-%m-%d')
                                    except ValueError:
                                        type_check = False

                            if type_check is False:
                                return HttpResponse('Error 400: Parameters are of incorrect type.', status=400)

                            query_string = replace_variables(api_calls[callType].get('query'), param_list, avail_params)

                            json_obj = get_json_from_backend(query_string)

                            return HttpResponse(json.dumps(json_obj), content_type="application/json")

                else:
                    return HttpResponse('Error 400: No parameters defined', status=400)

            else:
                return HttpResponse('Error 429: Throttling or Metering limit reached', status=429)

        else:
            return HttpResponse('Error 401: Unauthorized, require email & API key', status=401)

    return HttpResponseNotFound(request)


# document HTML page
def documentation(request):
    return render(request, 'documentation.html')
