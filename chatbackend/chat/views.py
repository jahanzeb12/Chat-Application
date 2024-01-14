from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
import json
from .models import Room, ChatUser

@csrf_exempt
def create_room_with_users(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id1 = data.get('user_id1')
            user_id2 = data.get('user_id2')
            room_name = data.get('room_name')

            user1 = ChatUser.objects.get(pk=user_id1)
            user2 = ChatUser.objects.get(pk=user_id2)

            if user1 == user2:
                raise ValidationError("Cannot add the same user twice.")

            room, created = Room.objects.get_or_create(name=room_name)
            # Call full_clean() to validate the room instance
            # room.full_clean()
            # Explicitly save the room to ensure it's committed to the database
            room.save()

            if room.participants.count() >= 2:
                raise ValidationError("This room already has the maximum number of participants.")

            if not room.participants.filter(pk=user1.pk).exists():
                room.participants.add(user1)
            if not room.participants.filter(pk=user2.pk).exists():
                room.participants.add(user2)

            return JsonResponse({'status': 'success', 'room_id': room.id})
        except ValidationError as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
        except ChatUser.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'One or both users not found.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
