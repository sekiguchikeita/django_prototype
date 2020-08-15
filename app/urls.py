from django.contrib import admin
from django.conf.urls import url
from . import views
from django.urls import path, include


urlpatterns = [
    url(r'^$',views.home, name='home'),
    path('create/', views.create, name='create'),
    path('admin/', admin.site.urls),
    # path('',views.homepage,name='homepage'),
    # path('send_Request/',views.send_request,name='send_request'),
    path('index/',views.index,name='index'),
    ]


