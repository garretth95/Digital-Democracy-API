from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from . import templates
from .forms import UserForm
from .models import User
from itsdangerous import URLSafeSerializer


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

            s = URLSafeSerializer('secret-key')
            key = s.dumps(user_dict.get('email'))


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

