from django.urls import path

from vehicle.views.vehicle import VehicleView, VehicleDetailView

urlpatterns = [
    path('', VehicleView.as_view(), name='vehicle_view'),
    path('/<id>', VehicleDetailView.as_view(), name='vehicle_detail_view'),
]
