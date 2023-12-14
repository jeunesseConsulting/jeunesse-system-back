from django.urls import path

from service.views.service import ServiceView, ServiceDetailView


urlpatterns = [
    path('', ServiceView.as_view(), name='service_view'),
    path('/<id>', ServiceDetailView.as_view(), name='service_detail_view'),
]

