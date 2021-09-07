import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from django.db.models.signals import post_save, post_delete, pre_save
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import StringModel


class Consumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        post_save.connect(self.send_db_update, StringModel)

    def receive(self, text_data):
        pass

    def diconnect(self, event):
        print("Disonnect ", event)

    def send_db_update(self, instance, **kwargs):
        self.send(instance.data)
