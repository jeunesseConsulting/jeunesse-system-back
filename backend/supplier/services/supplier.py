from backend.abstracts.services import AbstractServices

from supplier.models import Supplier


class SupplierServices(AbstractServices):

    model = Supplier
