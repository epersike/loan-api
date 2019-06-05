from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ContractSerializer, PaymentSerializer
from .models import Contract, Payment

# Create your views here.

class ContractViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contracts to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Contract.objects.all().order_by('ts_subscription')
    serializer_class = ContractSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows payments to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Payment.objects.all().order_by('payment_original_date')
    serializer_class = PaymentSerializer

    def create(self, *args, **kwargs):
        return super(PaymentViewSet, self).create(*args, **kwargs)

