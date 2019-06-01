from .models import Contract, Payment
from rest_framework import serializers


class ContractSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contract
        fields = ('total_amount', 'qty_payment', 'interest_rate','ip_address', 'ts_subscription', 'bank_name', 'customer_name')


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'payment_original_date', 'payment_date', 'subtotal', 'total', 'contract')