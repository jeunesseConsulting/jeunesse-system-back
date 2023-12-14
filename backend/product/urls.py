from django.urls import path

from product.views.type import ProductTypeView, ProductTypeDetailView
from product.views.measure_unit import ProductMeasureUnitView, ProductMeasureUnitDetailView
from product.views.product import ProductView, ProductDetailView

urlpatterns = [
    path('/types', ProductTypeView.as_view(), name='product_type'),
    path('/types/<id>', ProductTypeDetailView.as_view(), name='detail_product_type'),
    path('/measure-units', ProductMeasureUnitView.as_view(), name='product_measure_unit'),
    path('/measure-units/<id>', ProductMeasureUnitDetailView.as_view(), name='detail_product_measure_unit'),
    path('', ProductView.as_view(), name='product_view'),
    path('/<id>', ProductDetailView.as_view(), name='product_detail_view'),
]
