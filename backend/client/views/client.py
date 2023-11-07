from backend.abstracts.views import AuthenticatedAPIView
from rest_framework.response import Response
from rest_framework import status

from client.services.client import ClientServices
from client.serializer import ClientSerializer


class ClientView(AuthenticatedAPIView):


    def get(self, request):
        clients = ClientServices.query_all()
        serializer = ClientSerializer(clients, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serializer = ClientSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ClientDetailView(AuthenticatedAPIView):


    def get(self, request, id):
        client = ClientServices.get(id)

        if client:
            serializer = ClientSerializer(client)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, id):
        client = ClientServices.get(id)

        if client:
            serializer = ClientSerializer(client, request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, id):
        client = ClientServices.get(id)

        if client:
            client.delete()
            return Response(data={'message':'client deleted'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
