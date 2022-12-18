from django.urls import path

from app.api.views import ProductoList, ProductoDetalle, ProductoListado, ProductoCrear,\
    ProductoEditar, ProductoEliminar

urlpatterns = [
     # url de borjorge
    path('borjorge/v1/productos/', ProductoList.as_view(),name='producto_list' ),

    #--Esta url me parmite en una sola pasado el id del registro editar y/o eliminar 
    path('borjorge/v1/productos/<int:pk>', ProductoDetalle.as_view(),name='producto_detalle' ),

    
    
    # url de santa cruz
    path('santacruz/v2/productos/listado', ProductoListado.as_view(),name='productolistado' ),
    path('santacruz/v2/productos/crear', ProductoCrear.as_view(),name='productocrear' ),
    path('santacruz/v2/productos/editar/<int:pk>', ProductoEditar.as_view(),name='productoeditar' ),
    path('santacruz/v2/productos/eliminar/<int:pk>', ProductoEliminar.as_view(),name='productoeliminar' ),
]
