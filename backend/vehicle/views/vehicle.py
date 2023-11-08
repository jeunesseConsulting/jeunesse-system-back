from backend.abstracts.views import AuthenticatedAPIView, AuthenticatedDetailAPIView

from vehicle.services.vehicle import VehicleServices
from vehicle.serializer import VehicleCreateSerializer, VehicleSerializer

from rest_framework.response import Response
from rest_framework import status


class VehicleView(AuthenticatedAPIView):


    model_serializer = VehicleSerializer
    model_service = VehicleServices

    def post(self, request):
        data = request.data
        serializer = VehicleCreateSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            vehicle = self.model_service.get(serializer.instance.id)
            response_serializer = self.model_serializer(vehicle)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        
    
class VehicleDetailView(AuthenticatedDetailAPIView):


    model_serializer = VehicleSerializer
    model_service = VehicleServices

    def put(self, request, id):
        vehicle = self.model_service.get(id)
        data = request.data

        if vehicle:
            serializer = VehicleCreateSerializer(vehicle, data=data, partial=True)
            if serializer.is_valid():
                vehicle = self.model_service.get(serializer.instance.id)
                response_serializer = self.model_serializer(vehicle)
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)

