from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    key = models.CharField(max_length=200)
    user_group = models.CharField(max_length=200)
