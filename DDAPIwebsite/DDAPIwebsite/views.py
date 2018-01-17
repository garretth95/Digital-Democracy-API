from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
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
    print(test_get_bill_text())  # THIS IS FOR TESTING, WILL REMOVE
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

# # @api_view(['GET'])
# def bill_text(request, bid):
#
#     # if not bid:
#     #     try:
#     #         # get(bid=bid)
#     #
#     #     except: # bill doesn't exist
#     #
#     #
#     #     if request.method == 'GET':
#     #         return
#     #
#     # else:
#     #     return HttpResponseNotFound
#     # return '<h1>' + bid + '</h1>'



