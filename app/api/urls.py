from django.urls import path

from rest_framework.routers import DefaultRouter

from app.api.views import ProductoList, ProductoDetalle, ProductoListado, ProductoCrear,\
    ProductoEditar, ProductoEliminar, CategoriaList, SubCategoriaList, CategoriaDetalle, ProductoViewSet


router = DefaultRouter()
router.register('v1/productos', ProductoViewSet)

urlpatterns = [
     # url de borjorge
    path('borjorge/v1/productos/', ProductoList.as_view(),name='producto_list' ),

    path('borjorge/v1/categorias/', CategoriaList.as_view(),name='categoria_list' ),

    #path('borjorge/v1/subcategorias/', SubCategoriaList.as_view(),name='subcategoria_list' ),

    #--Esta url me parmite en una sola pasado el id del registro editar y/o eliminar 
    path('borjorge/v1/productos/<int:pk>', ProductoDetalle.as_view(),name='producto_detalle' ),

    path('borjorge/v1/categorias/<int:pk>', CategoriaDetalle.as_view(),name='categoria_list' ),
    path('borjorge/v1/categorias/<int:pk>/subcategorias/', SubCategoriaList.as_view(),name='categoria_list' ),

    
    
    # url de santa cruz
    path('santacruz/v2/productos/listado', ProductoListado.as_view(),name='productolistado' ),
    path('santacruz/v2/productos/crear', ProductoCrear.as_view(),name='productocrear' ),
    path('santacruz/v2/productos/editar/<int:pk>', ProductoEditar.as_view(),name='productoeditar' ),
    path('santacruz/v2/productos/eliminar/<int:pk>', ProductoEliminar.as_view(),name='productoeliminar' ),
]

urlpatterns += router.urls
