from django.urls import path
from . import views

app_name = 'dashboard'  # This should be a string

urlpatterns = [
    path('', views.index, name='index'),
]
