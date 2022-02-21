from django.urls import path
from .views import *

urlpatterns = [
    path('profile', ProfileView.as_view()),
    path('profile/<int:id>', ProfileDetail.as_view()),
    path('apps', Apps.as_view()),
    path('apps/<int:id>', AppsDetail.as_view()),
    path('sub_apps', Sub_Apps_View.as_view()),
    path('sub_apps/<int:id>', SupAppDetail.as_view()),
]