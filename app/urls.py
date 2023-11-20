from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns=[
      path('index',views.index,name='index'),
      path('register',views.register,name='register'),
      path('login',views.handlelogin,name='handlelogin'),
      path('logout',views.handlelogout, name='handlelogout'),
      path('index2',views.index2),
      path('index3',views.index3),
      path('index4',views.index4),
      path('index5',views.index5),

    ]
