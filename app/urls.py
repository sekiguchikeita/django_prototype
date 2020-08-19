from django.contrib import admin
from django.conf.urls import url
from . import views
from django.urls import path, include
#スクレイピング
from django.urls import path
from .views import Create, listfunc



urlpatterns = [
    url(r'^$',views.home, name='home'),
    path('create/', views.create, name='create'),
    path('admin/', admin.site.urls),
    # path('',views.homepage,name='homepage'),
    # path('send_Request/',views.send_request,name='send_request'),
    # path('index/',views.index,name='index'),
   #スクレイピング
    path('', Create.as_view(), name='home'),
    path('list/', listfunc, name='list'),
    ]


