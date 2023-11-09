from rest_framework import serializers


from product.models import Product, ProductMeasureUnit, ProductType
from product.aux_models import OrderProducts


class ProductTypeSerializer(serializers.ModelSerializer):


    class Meta:
        model = ProductType
        fields = '__all__'


class ProductMeasureUnitSerializer(serializers.ModelSerializer):


    class Meta:
        model = ProductMeasureUnit
        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):


    measure_unit = ProductMeasureUnitSerializer()
    type = ProductTypeSerializer()

    class Meta:
        model = Product
        fields = '__all__'


class OrderProductsCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = OrderProducts
        fields = '__all__'


class OrderProductsSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = OrderProducts
        fields = '__all__'

