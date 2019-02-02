"""Messenger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from chat_app.views import AuthView, MessengerView, RestAPIView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', AuthView.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^messenger/$', MessengerView.index),
    url(r'^login/$', login, {'template_name':'chat_app/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name':'chat_app/logout.html'}, name='logout'),
    url(r'^signup/$', AuthView.signup, name='signup'),

    url(r'^api/users_list/$', RestAPIView.UsersList.as_view(), name='users_list'),
    url(r'^api/msgs_logs/$', RestAPIView.MessagesList.as_view(), name='msgs_logs'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
