from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status

from backend.exceptions import DataBaseException


class AuthenticatedAPIView(APIView):


    permission_classes = [IsAuthenticated]
    model_service = None
    model_serializer = None

    def get(cls, _):
        try:
            objs = cls.model_service.query_all()
            serializer = cls.model_serializer(objs, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except DataBaseException:
            return Response({'message':'unexpected database error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
        except Exception:
            return Response({'message':'unexpected error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    
    def post(cls, request):
        try:
            data = request.data
            serializer = cls.model_serializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception:
            return Response({'message':'unexpected error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        

class AuthenticatedDetailAPIView(APIView):


    permission_classes = [IsAuthenticated]
    model_service = None
    model_serializer = None

    def get(cls, _, id):
        try:
            obj = cls.model_service.get(id)

            if obj:
                serializer = cls.model_serializer(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
        except DataBaseException:
            return Response({'message':'unexpected database error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
    def put(cls, request, id):
        try:
            obj = cls.model_service.get(id)

            if obj:
                serializer = cls.model_serializer(obj, request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)

                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
        except DataBaseException:
            return Response({'message':'unexpected database error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
    def delete(cls, _, id):
        try:
            obj = cls.model_service.get(id)

            if obj:
                obj.delete()
                return Response(data={'message': 'object deleted'}, status=status.HTTP_204_NO_CONTENT)

            return Response(data={'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
        except DataBaseException:
            return Response({'message':'unexpected database error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

