from backend.abstracts.views import AuthenticatedAPIView, AuthenticatedDetailAPIView
from backend.exceptions import DataBaseException

from vehicle.services.vehicle import VehicleServices
from vehicle.serializer import VehicleCreateSerializer, VehicleSerializer

from rest_framework.response import Response
from rest_framework import status


class VehicleView(AuthenticatedAPIView):


    model_serializer = VehicleSerializer
    model_service = VehicleServices

    def post(self, request):
        try:
            data = request.data
            serializer = VehicleCreateSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                vehicle = self.model_service.get(serializer.instance.id)
                response_serializer = self.model_serializer(vehicle)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except DataBaseException:
            return Response({'message':'unexpected database error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
        except Exception:
            return Response({'message':'unexpected error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
    
class VehicleDetailView(AuthenticatedDetailAPIView):


    model_serializer = VehicleSerializer
    model_service = VehicleServices

    def put(self, request, id):
        try:
            vehicle = self.model_service.get(id)
            data = request.data

            if vehicle:
                serializer = VehicleCreateSerializer(vehicle, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    vehicle = self.model_service.get(serializer.instance.id)
                    response_serializer = self.model_serializer(vehicle)
                    return Response(response_serializer.data, status=status.HTTP_200_OK)

                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
        except DataBaseException:
            return Response({'message':'unexpected database error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
        except Exception:
            return Response({'message':'unexpected error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

