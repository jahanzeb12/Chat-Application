from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class ChatUser(models.Model):

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    email_id = models.CharField(max_length=100, null=True,blank=True)
    name = models.CharField(max_length=50, null=True,blank=True)

    def __str__(self):
        return str(self.user)

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    participants = models.ManyToManyField(ChatUser, related_name='chat_rooms', blank=True)

    def __str__(self):
        return self.name

    # def clean(self):
    #     # Ensure that no more than two users are in a room
    #     if self.participants.count() > 2:
    #         raise ValidationError("A room cannot have more than two participants")

    # def save(self, *args, **kwargs):
    #     self.clean()
    #     super().save(*args, **kwargs)

class Message(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text