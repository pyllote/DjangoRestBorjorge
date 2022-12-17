from django.contrib import admin
from .models import Categoria, SubCategoria, Producto





class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['descripcion']
    list_display = ('id','descripcion')


class SubCategoriaAdmin(admin.ModelAdmin):
    search_fields = ['descripcion']
    list_display = ('id','categoria','descripcion')
    

class SubCategoriaAdmin(admin.ModelAdmin):
    search_fields = ['descripcion']
    list_display = ('id','categoria','descripcion')


class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['descripcion']
    list_display = ('id','subcategoria','descripcion','fecha_creado','vendido')



# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(SubCategoria, SubCategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)