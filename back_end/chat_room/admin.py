from django.contrib import admin
from chat_room.models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """Комнаты чата"""
    list_display = ("creator", "invited_user", "date")

    def invited_user(self, obj):
        return "\n".join([user.username for user in obj.invited.all()])

