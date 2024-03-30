from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponseRedirect, JsonResponse
from .models import Message, Chat

# Create your views here.
DEFAULT_LOGIN_REDIRECT = "/chat/"

@login_required(login_url="/chat/login")
def index(request):
    """Renders the chat
    """
    if request.method == "POST":
        chat = Chat.objects.get(pk=1)
        message = Message.objects.create(text=request.POST["message"], chat=chat, author=request.user, receiver=request.user)
        data = serializers.serialize("json", [message, ])
        return JsonResponse({"message": data[1:-1]})
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
        next = request.GET.get("next", DEFAULT_LOGIN_REDIRECT)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(next)
        else:
            return render(request, "chat/login.html",{ "error_message": "Invalid username and/or password. Please try again.", "next": next })
        
def register(request):
    if request.method == "GET":
        return render(request, "chat/register.html")
    password = request.POST["password"]
    if not password == request.POST["password2"]:
        return render(request, "chat/register.html", {"error_message": "Passwörter stimmen nicht überein."})
    User = get_user_model()
    username = request.POST["username"]
    email = request.POST["email"]
    user = User.objects.create_user(username, email, password)
    user = authenticate(request, username=username, password=password)
    login(request, user)
    return HttpResponseRedirect("/chat/")