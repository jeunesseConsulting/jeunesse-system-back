from backend.abstracts.views import AuthenticatedAPIView, AuthenticatedDetailAPIView
from rest_framework.response import Response
from rest_framework import status

from permissions.services.permission import PermissionsServices
from permissions.serializer import PermissionsSerializer


class PermissionsView(AuthenticatedAPIView):


    model_service = PermissionsServices
    model_serializer = PermissionsSerializer
        

class PermissionsDetailView(AuthenticatedDetailAPIView):


    model_service = PermissionsServices
    model_serializer = PermissionsSerializer

