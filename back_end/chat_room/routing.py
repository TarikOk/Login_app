from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<int:hash_id>/', consumers.FooConsumer),
]
