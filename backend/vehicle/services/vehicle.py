from backend.abstracts.services import AbstractServices

from vehicle.models import Vehicle


class VehicleServices(AbstractServices):


    model = Vehicle

    def client_vehicles(id):
        try:
            vehicles = Vehicle.objects.filter(owner=id)
            return vehicles
        except Vehicle.DoesNotExist:
            return None
