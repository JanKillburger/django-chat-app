from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
  path("", views.index),
  path("login", views.login_view),
  path("logout", views.logout_view),
  path("register", views.register),
]