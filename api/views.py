from django.shortcuts import render, redirect, get_object_or_404
import pandas as pd
from django.http import HttpResponseRedirect, JsonResponse
from telethon import TelegramClient
from asgiref.sync import async_to_sync
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest,GetContactsRequest
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import time
import math
name= 'Juwel Rana'
api_id = '2340381'
api_hash='af24eb2ad4b5b9e90699cf8deb6aeecb'
check_list={}
@async_to_sync
async def get_group_data(request):
    data={}
    selected_id = int(request.GET['selected_list'])
    async with TelegramClient(name, api_id, api_hash) as client:
        if selected_id != -1:
            part = await client.get_participants(selected_id)
            for i in part:
                if i.last_name != None:
                    username=i.first_name+" "+i.last_name
                else:
                    username=i.first_name
                data[i.id]=username
                #print(i.id)
        else:
            contacts = await client(GetContactsRequest(hash=0))
            for i in range(len(contacts.users)):
                if contacts.users[i].id not in check_list:
                    if contacts.users[i].last_name!=None:
                        username = contacts.users[i].first_name + " " + contacts.users[i].last_name
                    else:
                        username=contacts.users[i].first_name
                    data[contacts.users[i].id] = username
        print("ok")
    return JsonResponse({"data":data})
@async_to_sync
async def sendMessage(request):
    text_message=request.GET['text_message']
    selected_id=request.GET['selected_id']
    data=''
    try:
        async with TelegramClient(name, api_id, api_hash) as client:
            await client.send_message(selected_id, text_message)
    except:
        data=str(selected_id)
    return JsonResponse({"data":data})
@async_to_sync
async def search(request):
    result={}
    result[-1]="All"
    hash={}
    async with TelegramClient(name, api_id, api_hash) as client:
       async for dialog in client.iter_dialogs():
           result[dialog.id] = dialog.title
           #hash[dialog.id]=dialog.entity.access_hash
    return JsonResponse({"data":result,"hash":hash})

@async_to_sync
async def add_contact_data(request):
    s=''
    error=''
    try:
        number=str(request.GET['number'])
        username=request.GET['username']
        name_extension=request.GET['extension']
        async with TelegramClient(name, api_id, api_hash) as client:
            contact = InputPhoneContact(client_id=0, phone=number,
                                        first_name=username,
                                        last_name=name_extension,
                                        add_phone_privacy_exception=True)

            result = await client(ImportContactsRequest(contacts=[contact]))
            if len(result.users) == 0:
                s = username + " (" + number + ")"
    except:
        error='Server Problem'
    return JsonResponse({"data":s,'error':error})

@async_to_sync
async def add_group_member_data(request):
    s=''
    error=''
    try:
        number=str(request.GET['number'])
        group=int(request.GET['group'])
        async with TelegramClient(name, api_id, api_hash) as client:
            entity = await client.get_entity(number)
            await client(AddChatUserRequest(chat_id=group,user_id=entity, fwd_limit=0))
    except:
        error='Entity is not Found..'
        s=number
    return JsonResponse({"data":s,'error':error})
def xlsx_data_request(request):
    path=request.GET['path']
    all_data=[]
    error=''
    try:
        dfs = pd.read_excel(path, engine="openpyxl")
        for number in dfs['mobile number']:
            if str(number) != 'nan':
                print(number)
                all_data+=[number]
            else:
                break
    except:
        error='Excel File not Found'
    context={
        "data":all_data,
        'error':error,
    }
    return JsonResponse(context)

@async_to_sync
async def add_group_member_request(request):
    return JsonResponse({"data":''})
@async_to_sync
async def add_channel_member_data(request):
    s = ''
    error = ''
    try:
        number = str(request.GET['number'])
        group = int(request.GET['group'])
        async with TelegramClient(name, api_id, api_hash) as client:
            target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)
            entity = await client.get_entity(number)
            user_to_add = InputPeerUser(user['id'], user['access_hash'])
            client(InviteToChannelRequest(target_group_entity, [user_to_add]))
            print("Waiting 60 Seconds...")
            time.sleep(60)
    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
    except UserPrivacyRestrictedError:
        print("The user's privacy settings do not allow you to do this. Skipping.")
    except:
        error = 'Entity is not Found..'
        s = number
    return JsonResponse({"data": s, 'error': error, 'list': [group, entity.id]})
def telegram(request):
    return render(request, 'telegram.html', {})
def add_contact(request):
    return render(request,'add_contact.html',{})
def add_group_member(request):
    return render(request,'add_group_member.html',{})
def add_channel_member(request):
    return render(request,'add_channel_member.html',{})
def sendMessage_xlsx(request):
    return render(request,'send_message_xlsx.html',{})
# def saved_post(request):
#
#     return render(request, 'savedposts.html', context)
#
# # get post coordinate...
# def get_near_post_coordinator(request):
#     latitude = request.GET['latitude']
#     longitude = request.GET["longitude"]
#     obj = Post.objects.filter(temporary_latitude__isnull=False).values()
#     data = list(obj)
#     return JsonResponse(data, safe=False)
