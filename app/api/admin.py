from django.contrib import admin
from .models import Categoria, SubCategoria





class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['descripcion']
    list_display = ('id','descripcion')


class SubCategoriaAdmin(admin.ModelAdmin):
    search_fields = ['descripcion']
    list_display = ('id','categoria','descripcion')
    



# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(SubCategoria, SubCategoriaAdmin)