from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status


class AuthenticatedAPIView(APIView):


    permission_classes = [IsAuthenticated]
    model_service = None
    model_serializer = None

    def get(cls, request):
        objs = cls.model_service.query_all()
        serializer = cls.model_serializer(objs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(cls, request):
        data = request.data
        serializer = cls.model_serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class AuthenticatedDetailAPIView(APIView):


    permission_classes = [IsAuthenticated]
    model_service = None
    model_serializer = None

    def get(cls, request, id):
        obj = cls.model_service.get(id)

        if obj:
            serializer = cls.model_serializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(cls, request, id):
        obj = cls.model_service.get(id)

        if obj:
            serializer = cls.model_serializer(obj, request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(cls, request, id):
        obj = cls.model_service.get(id)

        if obj:
            obj.delete()
            return Response(data={'message': 'object deleted'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)

