from django.conf.urls import url
from . import views
from django.urls import path, include

urlpatterns = [
    url(r'^$',views.home, name='home'),
    path('create', views.create, name='create'),
    ]


