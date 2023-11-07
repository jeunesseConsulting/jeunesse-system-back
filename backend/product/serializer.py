from rest_framework import serializers


from product.models import Product, ProductMeasureUnit, ProductType


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
