from rest_framework import viewsets
from .serializers import ContractSerializer, PaymentSerializer
from .models import Contract, Payment

# Create your views here.

class ContractViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contracts to be viewed or edited.
    """
    queryset = Contract.objects.all().order_by('ts_subscription')
    serializer_class = ContractSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows payments to be viewed or edited.
    """
    queryset = Payment.objects.all().order_by('payment_original_date')
    serializer_class = PaymentSerializer