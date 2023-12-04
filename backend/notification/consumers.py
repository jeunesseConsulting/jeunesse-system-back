
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("notification_group", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("notification_group", self.channel_name)

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {str(e)}")
            return

        message = text_data_json.get('message', '')

        await self.channel_layer.group_send(
            "notification_group",
            {
                'type': 'send_notification',
                'message': message
            }
        )

    async def send_notification(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))