import os

from starlette.middleware.cors import CORSMiddleware

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

websocket_application = get_wsgi_application()
application = CORSMiddleware(websocket_application, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
