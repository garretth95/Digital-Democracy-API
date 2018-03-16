from django.db import models


# UserGroup is the Access Control List
# each user, once created, will have a default user access group (id=1)
# once verified for payment, can be changed by admin to different user group

class UserGroup(models.Model):
    group_id = models.IntegerField(primary_key=True)
    metering_rate = models.IntegerField()
    throttling_rate = models.IntegerField()


# User is associated to each user that uses the Digital Democracy API
# holds name, email, api key, user group (default when created)
# and request counts per minute, and day, and timestamp of latest request

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    key = models.CharField(max_length=200)
    user_group = models.ForeignKey(UserGroup)
    day_request_count = models.IntegerField(default=0)
    minute_request_count = models.IntegerField(default=0)
    latest_request = models.DateTimeField(null=True, blank=True)
