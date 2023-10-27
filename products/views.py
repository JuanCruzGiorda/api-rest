from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer, PedidoSerializer, DetalleSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = PedidoSerializer


class DetalleViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = DetalleSerializer