from django import forms


# get data from user on website to add to user database
class UserForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=200)
    last_name = forms.CharField(label='Last Name', max_length=200)
    email = forms.EmailField()

