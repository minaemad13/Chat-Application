from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# Create your views here.
from .consumers import redis_conn
from django.contrib.auth.decorators import login_required


def list_rooms(username):
    all_keys = redis_conn.keys('*')
    list_keys = [key.decode('utf-8') for key in all_keys if redis_conn.type(key) == b'list']

    set_with_username = set()
    for key in list_keys:
        list_elements = redis_conn.lrange(key, 0, -1)  # Get all elements in the list
        for element in list_elements:
            if username in element.decode('utf-8'):
                set_with_username.add(key)

    return list(set_with_username)

@login_required
def home(request):
    username = request.user.username
    list_set=list_rooms(username)
    return render(request,'main.html',{'title':'chat App' , 'all_chats' :list_set , 'username': request.user.username ,'inroom':False})


@login_required
def room(request, room_name):
    
    list_set=list_rooms(request.user.username)
    list_set.append(room_name)
    set_add_username = set(list_set)
    list_set=list(set_add_username)
    return render(request,'main.html',{'title':'chat App' , 'all_chats' :list_set,"room_name": room_name , 'username': request.user.username ,'inroom':True})
