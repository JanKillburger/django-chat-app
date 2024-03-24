from django.shortcuts import render
from .models import Message, Chat

# Create your views here.

def index(request):
    if request.method == "POST":
        chat = Chat.objects.get(pk=1)
        Message.objects.create(text=request.POST["message"], chat=chat, author=request.user, receiver=request.user)
    return render(request, 'chat/index.html', {'username': 'Jan'})