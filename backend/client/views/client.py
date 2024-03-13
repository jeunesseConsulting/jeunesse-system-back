from backend.abstracts.views import AuthenticatedAPIView
from backend.exceptions import DataBaseException

from rest_framework.response import Response
from rest_framework import status

from client.services.client import ClientServices
from client.serializer import ClientSerializer

from vehicle.services.vehicle import VehicleServices


class ClientView(AuthenticatedAPIView):


    model_service = ClientServices
    model_serializer = ClientSerializer
        

class ClientDetailView(AuthenticatedAPIView):


    def get(self, request, id):
        client = ClientServices.get(id)
        vehicles_param = str(request.query_params.get('vehicles')).lower()

        if client:
            serializer = ClientSerializer(client)
            vehicles = 1
            if vehicles_param == 'true':
                data = serializer.data
                
                try:
                    vehicles = VehicleServices.client_vehicles(client.id)

                except DataBaseException:
                    return Response({'message':'unexpected database error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

                vehicles_data = [
                    {
                        'id':vehicle.id,
                        'plate':vehicle.plate,
                        'color':vehicle.color,
                        'brand':vehicle.brand,
                        'model':vehicle.model,
                        'fabrication_year':vehicle.fabrication_year,
                        'type':vehicle.type
                    }
                    for vehicle in vehicles
                ]
                data['vehicles'] = vehicles_data
                return Response(data=data, status=status.HTTP_200_OK)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, id):
        client = ClientServices.get(id)

        if client:
            serializer = ClientSerializer(client, request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, _, id):
        client = ClientServices.get(id)

        if client:
            client.delete()
            return Response(data={'message':'client deleted'}, status=status.HTTP_204_NO_CONTENT)

        return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
