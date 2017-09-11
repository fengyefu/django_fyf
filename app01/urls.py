"""django2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index$', views.index),
    url(r'^orm$', views.orm),
    url(r'^login$', views.login),
    url(r'^home$', views.Home.as_view()),
    url(r'^user_group$', views.user_group),
    url(r'^user_info$',views.user_info),
    url(r'^userdetail-(?P<nid>\d+)',views.user_detail),
    url(r'^groupdetail-(?P<nid>\d+)',views.group_detail),
    url(r'^userdel-(?P<nid>\d+)',views.user_del),
    url(r'^groupdel-(?P<nid>\d+)',views.group_del),
    url(r'^useredit-(?P<nid>\d+)',views.user_edit),
    # url(r'^detail', views.detail),
    url(r'^detail-(\d+).html', views.detail),
    # url(r'^detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail),
]
