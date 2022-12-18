from django.shortcuts import render

#--Realizamos la importación

from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer

# Create your views here.

#--Nota Borjorge utiliza vistas genéricas que permite crear y listar
#--Santa Cruz utiliza una para listar ListAPIView y otra para crear CreateAPIView

#--Aqui usamos lo de borjorge

class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
 
 
class ProductoDetalle(generics.RetrieveDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


#--Aqui usamos lo de Santa Cruz

class ProductoListado(generics.ListAPIView):
    serializer_class = ProductoSerializer
    def get_queryset(self):
        return Producto.objects.all()

class ProductoCrear(generics.CreateAPIView):
    serializer_class = ProductoSerializer


class ProductoEditar(generics.RetrieveUpdateAPIView):
    serializer_class = ProductoSerializer
    def get_queryset(self):
        return Producto.objects.all()


class ProductoEliminar(generics.DestroyAPIView):
    serializer_class = ProductoSerializer
    def get_queryset(self):
        return Producto.objects.all()