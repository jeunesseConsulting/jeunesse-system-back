from rest_framework import serializers

from purchase_order.models import PurchaseOrderStatus


class PurchaseOrderStatusSerializer(serializers.ModelSerializer):


    class Meta:
        model = PurchaseOrderStatus
        fields = '__all__'
