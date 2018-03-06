from django.db import models


class UserGroup(models.Model):
    group_id = models.IntegerField(primary_key=True)
    metering_rate = models.IntegerField()
    throttling_rate = models.IntegerField()


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    key = models.CharField(max_length=200)
    user_group = models.ForeignKey(UserGroup)


