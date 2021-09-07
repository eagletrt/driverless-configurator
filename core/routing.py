from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
# from channels.security.websocket import AllowedHostOriginValidator, OriginValidator

from Dashboard.consumers import Consumer

websocket_urlpatterns = [
    url("", Consumer.as_asgi()),
]
