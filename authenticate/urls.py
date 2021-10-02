from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin', views.signin, name='signin'),
    path('', views.welcome, name='welcome'),
    path('newuser', views.newuser, name='newuser'),
    path('guest', views.guest, name='guest'),
    path('signout', views.signout, name='signout'),
]
