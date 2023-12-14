from django.test import SimpleTestCase
from django.urls import reverse, resolve

from vehicle.views.vehicle import VehicleView, VehicleDetailView


class TestUrls(SimpleTestCase):


    def test_vehicle_url_is_resolved(self):
        url = reverse('vehicle_view')
        self.assertEquals(resolve(url).func.view_class, VehicleView)

    def test_vehicle_detail_url_is_resolved(self):
        url = reverse('vehicle_detail_view', kwargs={'id':1})
        self.assertEquals(resolve(url).func.view_class, VehicleDetailView)