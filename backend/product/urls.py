from django.urls import path

from product.views.type import ProductTypeView, ProductTypeDetailView

urlpatterns = [
    path('/types', ProductTypeView.as_view(), name='product_type'),
    path('/types/<id>', ProductTypeDetailView.as_view(), name='detail_product_type'),
]
