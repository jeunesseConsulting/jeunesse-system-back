from rest_framework import serializers

from purchase_order.models import PurchaseOrderStatus, PurchaseOrder
from purchase_order.aux_models import PurchaseOrderProducts

from product.serializer import ProductSerializer

from supplier.serializer import SupplierSerializer


class PurchaseOrderProductsCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = PurchaseOrderProducts
        fields = '__all__'


class PurchaseOrderProductsSerializer(serializers.ModelSerializer):


    product = ProductSerializer()

    class Meta:
        model = PurchaseOrderProducts
        fields = '__all__'


class PurchaseOrderStatusSerializer(serializers.ModelSerializer):


    class Meta:
        model = PurchaseOrderStatus
        fields = '__all__'


class PurchaseOrderSerializer(serializers.ModelSerializer):


    products = serializers.SerializerMethodField()
    status = PurchaseOrderStatusSerializer()
    supplier = SupplierSerializer()

    class Meta:
        model = PurchaseOrder
        fields = '__all__'

    def get_products(self, obj):
        if obj.products.exists():
            return PurchaseOrderProductsSerializer(obj.products, many=True).data
        else:
            return []
        

class PurchaseOrderCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = PurchaseOrder
        fields = '__all__'
