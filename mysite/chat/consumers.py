# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("skr scope22222", self.scope['url_route'])
        # self.room_name = self.scope['url_route']['kwargs']['room_name']
        # self.room_group_name = 'chat_%s' % self.room_name

        self.room_name = "seabed"
        self.group_name = "seabed_group"

        # Join room group
        print('channel name', self.channel_name)
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # Receive message from WebSocket,receive from websocket client.
    async def receive(self, text_data):
        """
        Receive message from WebSocket,receive from websocket client.
        :param text_data: data received from front.(client,websocket)
        :return:
        """
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print('message areeeeeee', message)

        # Send message to room group.
        # must be required, or other client can't receive message.
        print('room group name:', self.group_name)
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    # async def chat_message(self, event):
    #     print('event areareare', event)
    #     message = event['message']
    #
    #     # Send message to WebSocket
    #     await self.send(text_data=json.dumps({
    #         'message': message
    #     }))

    async def chat_message(self, event):

        # 接收的参数是从前端输入的数据，需要改成从后端接收参数，在视图函数里直接调用
        # data = {"server_status": "health_ok"}
        # ins = ChatConsumer.chat_message(data) 就可以实现将数据通过 websocket 主动推送。

        # event is defined in function receive.
        print('event message', event)

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': "6666666"
        }))
