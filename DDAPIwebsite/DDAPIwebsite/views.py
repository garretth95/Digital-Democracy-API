from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render
from . import templates
from .forms import UserForm
from .models import User
from itsdangerous import URLSafeSerializer
import time

from .queryDB import test_get_bill_text


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


def check_api_key(email, key):  # checks User DB to see if key matches email

    if User.objects.get(email=email).key == key:
        return True
    else:
        return False


# @api_view(['GET'])  # may need for api classes
def test_get(request):

    if request.method == 'GET':

        if 'HTTP_EMAIL' in request.META and 'HTTP_API_KEY' in request.META\
                and User.objects.filter(email=request.META.get('HTTP_EMAIL')).exists()\
                and check_api_key(request.META.get('HTTP_EMAIL'), request.META.get('HTTP_API_KEY')):

            # check that email & key are in header, email exists, and email matches key

            row = test_get_bill_text()  # will change
            response = JsonResponse({'bill': {'text': row}})  # return data in json form

            return HttpResponse(response)

        else:
            return HttpResponseRedirect('/no_access/')

    return HttpResponseNotFound


def no_access(request):
    return render(request, 'no_access.html')


