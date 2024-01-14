# messaging/tests/test_consumers.py
import json
from channels.testing import WebsocketCommunicator, ApplicationCommunicator
from django.test import TestCase
from .routing import websocket_urlpatterns
from chatbackend.asgi import application  # Update with your project name

class ChatConsumerTest(TestCase):
    async def connect_ws(self, path):
        communicator = WebsocketCommunicator(application, f"/ws/{path}")
        connected, _ = await communicator.connect()
        self.assertTrue(connected)
        return communicator

    async def test_receive_message(self):
        communicator = await self.connect_ws("chat/")

        # Send a message
        message = {'message': "Hello, World!"}
        await communicator.send_json_to(message)

        # Receive the message from the server
        response = await communicator.receive_json_from()

        # Check if the message is received correctly
        self.assertEqual(response["message"], "Hello, World!")

        # Close the connection
        await communicator.disconnect()
