from backend.abstracts.views import AuthenticatedAPIView, AuthenticatedDetailAPIView
from rest_framework.response import Response
from rest_framework import status

from roles.services.roles import RoleService
from roles.serializer import RoleSerializer


class RoleView(AuthenticatedAPIView):


    model_serializer = RoleSerializer
    model_service = RoleService
        

class RoleDetailView(AuthenticatedDetailAPIView):


    model_serializer = RoleSerializer
    model_service = RoleService
    