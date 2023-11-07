from django.urls import path

from client.views.client import ClientView, ClientDetailView

urlpatterns = [
    path('', ClientView.as_view(), name='client_view'),
    path('/<id>', ClientDetailView.as_view(), name='client_detail_view'),
]
