from django.urls import path
from . import views
app_name = 'post'

urlpatterns = [
    path('', views.blog, name='blog'),
]
