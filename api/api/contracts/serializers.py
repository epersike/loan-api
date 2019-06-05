from datetime import datetime
from .models import Contract, Payment
from rest_framework import serializers


class ContractSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.CharField(source='get_absolute_url', read_only=True)
    class Meta:
        model = Contract
        fields = ('id', 'total_amount', 'qty_payment', 'interest_rate','ip_address', 'ts_subscription', 'bank_name', 'customer_name','url')

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    payment_original_date = serializers.DateField(read_only=True, required=False)
    subtotal = serializers.DecimalField(decimal_places=2, max_digits=10, read_only=True, required=False)
    class Meta:
        model = Payment
        fields = ('id', 'payment_original_date', 'payment_date', 'subtotal', 'total', 'contract', 'url')

    def create(self, *args, **kwargs):

        contract_data = args[0]['contract']
        
        args[0]['subtotal'] = contract_data.total_amount / contract_data.qty_payment
        args[0]['payment_original_date'] = datetime.date(datetime.now())

        return super(PaymentSerializer, self).create(*args, **kwargs)