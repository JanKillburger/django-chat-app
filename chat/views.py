from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Message, Chat

# Create your views here.
DEFAULT_LOGIN_REDIRECT = "/chat/"

@login_required(login_url="/chat/login")
def index(request):
    if request.method == "POST":
        chat = Chat.objects.get(pk=1)
        Message.objects.create(text=request.POST["message"], chat=chat, author=request.user, receiver=request.user)
    messages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': messages})

def login_view(request):
    if request.method == "GET":
        next = request.GET.get("next", DEFAULT_LOGIN_REDIRECT)
        return render(request, "chat/login.html", {"next": next})
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect = request.GET.get("next", DEFAULT_LOGIN_REDIRECT)
            return HttpResponseRedirect(redirect)
        else:
            return render(request, "chat/login.html",{ "error_message": "Invalid username and/or password. Please try again." })