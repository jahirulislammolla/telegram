"""TelegramCustomApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from api.views import search, telegram, sendMessage, add_contact,add_contact_data, add_channel_member_data, \
    add_group_member, xlsx_data_request, add_group_member_data, add_channel_member, get_group_data,sendMessage_xlsx

urlpatterns = [
    path('', telegram, name='telegram'),
    path('add_contact_data/',add_contact_data, name='add_contact_data'),
    path('search/', search, name='search'),
    path('sendMessage/', sendMessage, name='sendMessage'),
    path('add_contact/', add_contact, name='add_contact'),
    path('add_group_member/', add_group_member, name='add_group_member'),
    path('xlsx_data_request/',xlsx_data_request, name='xlsx_data_request'),
    path('add_group_member_data/',add_group_member_data,name='add_group_member_data'),
    path('add_channel_member/',add_channel_member,name='add_channel_member'),
    path('add_channel_member_data/',add_channel_member_data, name='add_channel_member_data'),
    path('get_group_data/',get_group_data,name='get_group_data'),
    path('sendMessage_xlsx/',sendMessage_xlsx,name='sendMessage_xlsx')
]
