from datetime import datetime
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import redis

import pytz

redis_conn = redis.Redis(host='127.0.0.1', port=6379, db=0)
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        user = self.scope["user"]
        self.room_group_name = f"{self.room_name}"
        if user.is_authenticated:
            self.userName = user.username
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
            messages = redis_conn.lrange(self.room_group_name, 0, -1)
            if messages:
                for message in messages:
                    await self.send(text_data=message.decode('utf-8'))
            else:    
                await self.send(text_data='{"message": "No Messages Found."}')
            
            
            
            

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
                

        # Choose your desired timezone
        cairo_timezone = pytz.timezone('Africa/Cairo')

        # Get the current time in that timezone
        current_time = datetime.now(cairo_timezone)
        formatted_time = current_time.strftime("%I:%M %p")

        redis_conn.rpush(self.room_group_name, json.dumps({"message": message, "userName": self.userName , 'time' :formatted_time} ))
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message, "userName": self.userName , 'time' :formatted_time}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        userName = event["userName"]
        time = event["time"]
        await self.send(text_data=json.dumps({"message": message , 'userName':userName , 'time' :time}))