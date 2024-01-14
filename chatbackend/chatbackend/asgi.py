"""
ASGI config for chatbackend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from chat import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbackend.settings')

application = get_asgi_application()
application = ProtocolTypeRouter(
    {
        # to allow HTTP protocol
        "http": get_asgi_application(),
        # to allow websockets Protocol
        "websocket": URLRouter(
        routing.websocket_urlpatterns
    ),
    }
    )

