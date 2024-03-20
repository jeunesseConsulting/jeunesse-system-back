from backend.abstracts.services import AbstractServices

from financial.models import FinancialEntry


class FinancialEntryServices(AbstractServices):


    model = FinancialEntry
