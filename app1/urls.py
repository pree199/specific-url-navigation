from app1.views import *
from django.urls import path

app_name='namita'
urlpatterns=[
    path('dad/',dad,name='dad'),
]