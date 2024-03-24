from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .models import Message, Chat

# Create your views here.

def index(request):
    if request.method == "POST":
        chat = Chat.objects.get(pk=1)
        Message.objects.create(text=request.POST["message"], chat=chat, author=request.user, receiver=request.user)
    messages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': messages})

def loginView(request):
    if request.method == "GET":
        return render(request, "chat/login.html")
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print("username:", username)
        print("password:", password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/chat/")
        else:
            #return 'invalid login' message
            pass