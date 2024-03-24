from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Message, Chat, User

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
  list_display = ('created_at', 'author', 'receiver')
  search_fields = ('author',)

admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)
admin.site.register(User, UserAdmin)