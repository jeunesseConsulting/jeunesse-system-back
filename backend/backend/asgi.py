import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import notification.routing
from starlette.middleware.cors import CORSMiddleware

import ssl
ssl.match_hostname = lambda cert, hostname: True

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

websocket_application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            notification.routing.websocket_urlpatterns
        )
    ),
})

application = CORSMiddleware(websocket_application, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])