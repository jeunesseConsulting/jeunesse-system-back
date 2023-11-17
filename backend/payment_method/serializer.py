from rest_framework import serializers

from payment_method.models import PaymentMethod


class PaymentMethodSerializer(serializers.ModelSerializer):


    class Meta:
        model = PaymentMethod
        fields = '__all__'
