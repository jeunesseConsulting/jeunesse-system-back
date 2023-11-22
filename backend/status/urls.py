from django.urls import path

from status.views.status import StatusView, StatusDetailView

urlpatterns = [
    path('', StatusView.as_view(), name='status_view'),
    path('/<id>', StatusDetailView.as_view(), name='status_detail_view'),
]
