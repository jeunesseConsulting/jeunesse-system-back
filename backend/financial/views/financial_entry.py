from backend.abstracts.views import AuthenticatedAPIView, AuthenticatedDetailAPIView
from backend.exceptions import DataBaseException

from rest_framework.response import Response
from rest_framework import status

from financial.serializer import FinancialEntrySerializer
from financial.services.financial_entry import FinancialEntryServices


class FinancialEntryView(AuthenticatedAPIView):

    
    model_serializer = FinancialEntrySerializer
    model_service = FinancialEntryServices

    def get(self, request):
        entry_type = request.query_params.get('type')

        try:
            if entry_type:
                objs = FinancialEntryServices.type_filter(entry_type)
                serializer = FinancialEntrySerializer(objs, many=True)

                return Response(serializer.data, status=status.HTTP_200_OK)
            
            objs = FinancialEntryServices.query_all()
            serializer = FinancialEntrySerializer(objs, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except DataBaseException:
            return Response({'message':'unexpected database error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
            
        except Exception:
            return Response({'message':f'unexpected error'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)      


class FinancialEntryDetailView(AuthenticatedDetailAPIView):


    model_serializer = FinancialEntrySerializer
    model_service = FinancialEntryServices
