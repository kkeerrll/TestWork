from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Supplier, NetworkObject
from .serializers import SupplierSerializer, NetworkObjectSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        country = self.request.query_params.get('country')
        if country:
            queryset = queryset.filter(country=country)
        return queryset

class NetworkObjectViewSet(viewsets.ModelViewSet):
    queryset = NetworkObject.objects.all()
    serializer_class = NetworkObjectSerializer


