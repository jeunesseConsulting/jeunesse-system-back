from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from service_order.utils import generate_service_order_pdf

from backend.settings import CLIENT_NAME


class PDFGeneratorView(APIView):


    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.data:
            pdf64 = generate_service_order_pdf(request.data, CLIENT_NAME)
            return Response(data={'pdf':pdf64}, status=status.HTTP_200_OK)
    
        return Response(data={'message':'invalid data'})

