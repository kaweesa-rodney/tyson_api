from django.urls import path
from .views import *

urlpatterns = [
    path('profile', ProfileView.as_view()),
    path('profile/<int:id>', ProfileDetail.as_view()),
    path('apps', Apps.as_view()),
    path('apps/<int:id>', AppsDetail.as_view()),
    path('sub_apps', Sub_Apps_View.as_view()),
    path('sub_apps/<str:sub_app_name>', SupAppDetail.as_view()),
    path('register_user', System_Users.as_view()),
    path('update_user/<int:id>', SystemUserDetail.as_view()),
    path('user_activity', UserActivity.as_view()),
    path('user_apps/<str:uid>', UserApps.as_view()),
    path('user_sub_apps/<str:uid>', UserSubApps.as_view()),
]
