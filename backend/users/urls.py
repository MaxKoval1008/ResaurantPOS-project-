from django.urls import path

from .views import UserAllView

app_name = 'users'

urlpatterns = [

    path('user/', UserAllView.as_view()),



]