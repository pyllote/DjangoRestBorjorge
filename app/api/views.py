from django.shortcuts import render

#--Realizamos la importación

from rest_framework import generics
from .models import Producto, Categoria, SubCategoria
from .serializers import ProductoSerializer, CategoriaSerializer, SubCategoriaSerializer

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


class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
 
#class SubCategoriaList(generics.ListCreateAPIView):
#    queryset = SubCategoria.objects.all()
#    serializer_class = SubCategoriaSerializer


class CategoriaDetalle(generics.RetrieveDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class SubCategoriaList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = SubCategoria.objects.filter(categoria_id=self.kwargs["pk"])
        return queryset
    serializer_class = SubCategoriaSerializer




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