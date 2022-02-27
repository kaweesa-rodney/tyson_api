from django.shortcuts import render
from .serializers import *
import jwt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import permissions
from .models import *
from django.contrib.auth.hashers import make_password
from django.db.models import Q


# Create your views here.
#Applications
class Apps(ListCreateAPIView):

    serializer_class = AppSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Applications.objects.all()


class AppsDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = RetrieveUpdateDestroyAPIView
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"
    

    def get_queryset(self):
        return Applications.objects.all()



#sub applications
class Sub_Apps_View(ListCreateAPIView):

    serializer_class = SubAppSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save()

    
    def get_queryset(self):
        return Sub_Apps.objects.all()



class SupAppDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = SubAppSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "sub_app_name"
    

    def get_queryset(self):
        return Sub_Apps.objects.all()


#Profile
class ProfileView(ListCreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save()


    def get_queryset(self):
        return Profile.objects.all()


class ProfileDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated, )
    lookup_field = "id"

    def get_queryset(self):
        return Profile.objects.all()



#User Activity
class UserActivity(ListCreateAPIView):
    serializer_class = UsersActivitySerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return users_activity.objects.all()


class UserActivityDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = UsersActivitySerializer
    permission_classes = (permissions.IsAuthenticated, )
    lookup_field = "id"

    def get_queryset(self):
        return UserActivity.objects.all()



#LockTable
class LockTable(ListCreateAPIView):
    serializer_class = LockTableSerializer
    permission_classes = (permissions.IsAuthenticated, )
    
    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return Lock_Table.objects.all()



class LockTableDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = LockTableSerializer
    permission_classes = (permissions.IsAuthenticated, )
    lookup_field = "record_id"

    def get_queryset(self):
        return Lock_Table.objects.all()



#Maintenance
class Maintenance(ListCreateAPIView):
    serializer_class = MaintenanceSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        return "no creation"

    def get_queryset(self):
        return Maintenance.objects.all()




#System users
class System_Users(ListCreateAPIView):
    serializer_class = SystemUserSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(
            password = make_password(self.request.data['password'])
        )


    def get_queryset(self):
        return SystemUsers.objects.all()



class SystemUserDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = SystemUserSerializer
    permission_classes = (permissions.IsAuthenticated, )
    lookup_field = "id"

    def get_queryset(self):
        return SystemUsers.objects.all()



class UserApps(ListAPIView):
    serializer_class = AppSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        uid = self.kwargs['uid']
        return User.objects.raw("""
            SELECT DISTINCT a.id, a.app_name FROM users_profile p 
                    inner join users_sub_apps sa on sa.id=CAST(p.sub_app_id AS INTEGER)
                    inner join users_applications a on a.id= CAST(sa.app_id AS INTEGER)
                    WHERE p.user_id = %s and p.ruid_rights LIKE '%%R%%'
        """, [uid])



class UserSubApps(ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        uid = self.kwargs['uid']
        return User.objects.raw("""
            SELECT * FROM users_profile
            where user_id = %s and ruid_rights LIKE '%%R%%'
        """, [uid])
