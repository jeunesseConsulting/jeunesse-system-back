from backend.abstracts.services import AbstractServices
from backend.exceptions import DataBaseException

from financial.models import FinancialEntry


class FinancialEntryServices(AbstractServices):


    model = FinancialEntry

    def type_filter(type: str):
        try:
            return FinancialEntry.objects.filter(entry_type=type)
        
        except Exception:
            raise DataBaseException
