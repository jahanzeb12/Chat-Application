from django.contrib import admin

# Register your models here.
from .models import ChatUser,Room

class ChatUsers(admin.ModelAdmin):
    list_display = ('pk', 'name','email_id')
   
admin.site.register(ChatUser,ChatUsers)
admin.site.register(Room)