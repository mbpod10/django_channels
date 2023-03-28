from django.urls import re_path
from root.consumers import TextRoomConsumer

websocket_urlpatterns = [
    re_path('ws/test/', TextRoomConsumer.as_asgi())
]
    # re_path(r'^ws/(?P<room_name>[^/]+)/$', TextRoomConsumer.as_asgi()),
# the websocket will open at 127.0.0.1:8000/ws/<room_name>

