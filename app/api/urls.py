from django.urls import path

from app.api.views import ProductoList, ProductoDetalle, ProductoListado, ProductoCrear

urlpatterns = [
     # url de borjorge
    path('borjorge/v1/productos/', ProductoList.as_view(),name='producto_list' ),
    path('borjorge/v1/productos/<int:pk>', ProductoDetalle.as_view(),name='producto_detalle' ),

    # url de santa cruz
    path('santacruz/v2/productos/listado', ProductoListado.as_view(),name='productolistado' ),
    path('santacruz/v2/productos/crear', ProductoCrear.as_view(),name='productocrear' ),
    
]
