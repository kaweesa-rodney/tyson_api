from msilib.schema import Class
from operator import mod
from os import access
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_level = models.CharField(max_length=1)
    sub_app_id = models.CharField(max_length=2)
    ruid_rights = models.CharField(max_length=4)
    added_by = models.CharField(max_length=5, null=True)
    added_date = models.DateTimeField(default=datetime.now)


class SystemUsers(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)
    email = models.EmailField()
    added_by = models.CharField(max_length=1)
    added_on = models.DateTimeField(default=datetime.now)

class Applications(models.Model):
    app_name = models.CharField(max_length=100)


class Sub_Apps(models.Model):
    sub_app_name = models.CharField(max_length=255)
    app_id = models.CharField(max_length=10)
    sub_app_description = models.TextField()


class users_activity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reset_password_date = models.DateTimeField(null=True)
    update_password_date = models.DateTimeField(null=True)
    update_password_status = models.CharField(max_length=1)
    login_status = models.CharField(max_length=1, null=True)


class Lock_Table(models.Model):
    locked_by = models.CharField(max_length=30)
    record_id = models.CharField(max_length=10)
    lock_date = models.DateTimeField(null=True)


class Maintenance(models.Model):
    access_code = models.CharField(max_length=5)
    ip_addresses = models.TextField()
