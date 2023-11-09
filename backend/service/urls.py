from django.urls import path

from service.views.service import ServiceView, ServiceDetailView


urlpatterns = [
    path('', ServiceView.as_view(), name='services_view'),
    path('/<id>', ServiceDetailView.as_view(), name='services_detail_view'),
]

