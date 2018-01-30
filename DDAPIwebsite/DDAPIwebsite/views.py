from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from . import templates
from .forms import UserForm
from .models import User
from itsdangerous import URLSafeSerializer
import time
import json

from .queryDB import test_get_bill_text, hearing_transcript


def index(request):
    return render(request, 'index.html')


def request_access(request):
    return render(request, "request_access.html")


def new_user(request):

    # form submission, if GET then probably a refresh -> will redirect
    if request.method == 'POST':

        form = UserForm(request.POST)

        # if the form submitted is valid
        if form.is_valid():
            user_dict = form.cleaned_data

            s = URLSafeSerializer(user_dict.get('email'))
            key = s.dumps(str(int(time.time()*100)))

            user = User(first_name=user_dict.get('first_name'), last_name=user_dict.get('last_name'),
                        email=user_dict.get('email'), key=key, user_group='base user group')

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


def check_api_key(email, key):  # checks User DB to see if email exists and key matches email

    # print(email, key)

    if User.objects.filter(email=email).exists() and User.objects.get(email=email).key == key:
        return True
    else:
        return False


# @api_view(['GET'])  # may need for api classes
def test_get(request):

    if request.method == 'GET':

        if 'HTTP_EMAIL' in request.META and 'HTTP_API_KEY' in request.META\
                and check_api_key(request.META.get('HTTP_EMAIL'), request.META.get('HTTP_API_KEY')):

            # check that email & key are in header, email exists, and email matches key

            row = test_get_bill_text()
            return HttpResponse(json.dumps({'bill': {'text': row}, }), content_type="application/json")

        else:
            # return HttpResponseRedirect('/no_access/')
            return HttpResponse('Unauthorized', status=401)

    return HttpResponseNotFound(request)


def no_access(request):
    return render(request, 'no_access.html')


def hearing(request, hid):
    if request.method == 'GET' and hid is not None and int(hid) > 0:

        # print('hid', hid)

        if 'HTTP_EMAIL' in request.META and 'HTTP_API_KEY' in request.META\
                and check_api_key(request.META.get('HTTP_EMAIL'), request.META.get('HTTP_API_KEY')):

            try:
                sql_rows = hearing_transcript(hid)
            except TypeError:
                return HttpResponseNotFound

            if len(sql_rows) > 0:

                json_rows = []
                i = 1

                for row in sql_rows:
                    if row[0] is None:
                        name = {'name': 'NA'}
                    else:
                        name = {'name': {'last': row[1], 'first': row[0]}}
                    talk_time = {'time': {'start': row[2], 'end': row[3]}}
                    text = {'text': row[4]}

                    utterance = {'utterance ' + str(i): [name, talk_time, text]}
                    i += 1

                    json_rows.append(utterance)

                return HttpResponse(json.dumps({'Transcript for Hearing id ' + hid: json_rows}),
                                    content_type="application/json")

        else:
            return HttpResponse('Unauthorized', status=401)

    return HttpResponseNotFound(request)


