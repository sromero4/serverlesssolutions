import graphene
from graphene_django.filter import DjangoFilterConnectionField

from sss_backend.models.restaurant import Producto, ProductoType

class Query (object):
    all_producto = DjangoFilterConnectionField(ProductoType, orderBy=graphene.List(of_type=graphene.String))

    def resolve_all_producto(self, info, **kwargs):
        orderBy = kwargs.get('orderBy', None)
        if orderBy is None:
          return Producto.objects.all()
        else:        
          return Producto.objects.order_by(*orderBy)