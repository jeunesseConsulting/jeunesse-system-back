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


class PurchaseOrderProductsViewSerializer(serializers.ModelSerializer):


    product = ProductSerializer()

    class Meta:
        model = PurchaseOrderProducts
        fields = [
            'product',
            'price',
            'quantity'
        ]


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
            return PurchaseOrderProductsViewSerializer(obj.products, many=True).data
        else:
            return []
        

class PurchaseOrderCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = PurchaseOrder
        fields = '__all__'


class PurchaseOrderSummarySerializer(serializers.ModelSerializer):


    supplier = SupplierSerializer()
    status = PurchaseOrderStatusSerializer()

    class Meta:
        model = PurchaseOrder
        fields = [
            'supplier',
            'status',
            'delivery_date',
            'created_at',
        ]


class ProductPurchaseSummarySerializer(serializers.ModelSerializer):

    purchase_order = serializers.SerializerMethodField()
    product = ProductSerializer()

    class Meta:
        model = PurchaseOrderProducts
        fields = [
            'purchase_order',
            'product',
            'price',
            'quantity',
        ]

    def get_purchase_order(self, obj):
        if obj.purchase_order:
            purchase_order = PurchaseOrder.objects.filter(id=obj.purchase_order).first()
            return PurchaseOrderSummarySerializer(purchase_order).data
        else:
            return None
