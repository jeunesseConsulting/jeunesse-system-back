from django.urls import path

from payment_method.views.payment_method import PaymentMethodView, PaymentMethodDetailView

urlpatterns = [
    path('', PaymentMethodView.as_view(), name='payment_method_view'),
    path('/<id>', PaymentMethodDetailView.as_view(), name='payment_method_detail_view'),
]
