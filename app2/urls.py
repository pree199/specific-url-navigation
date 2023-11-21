from app2.views import *
from django.urls import path

app_name='panchu'
urlpatterns=[
    path('mom/',mom,name='mom'),
]