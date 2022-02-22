from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import *

class AppSerializer(ModelSerializer):

    class Meta:
        model = Applications
        fields = ['app_name']



class SubAppSerializer(ModelSerializer):

    class Meta:
        model = Sub_Apps

        fields = ['sub_app_name', 'app_id', 'sub_app_description']



class ProfileSerializer(ModelSerializer):

    class Meta:
        model = Profile

        fields = ['user', 'user_level', 'sub_app_id', 'ruid_rights', 'added_by', 'added_date']


class UsersActivitySerializer(ModelSerializer):

    class Meta:
        model = users_activity

        fields = ['user', 'reset_password_date', 'update_password_date', 'update_password_status', 'login_status']



class LockTableSerializer(ModelSerializer):

    class Meta:
        model = Lock_Table

        fields = ['locked_by', 'record_id', 'lock_date']



class MaintenanceSerializer(ModelSerializer):

    class Meta:
        model = Maintenance

        fields = ['access_code', 'ipaddresses']




class SystemUserSerializer(ModelSerializer):

    class Meta:
        model = SystemUsers

        fields = ['username', 'password', 'last_login', 'is_active', 'email', 'added_by', 'added_on']
