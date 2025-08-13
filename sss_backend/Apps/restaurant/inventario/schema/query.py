import graphene
from graphene_django.filter import DjangoFilterConnectionField

from sss_backend.models.restaurant import Inventario, InventarioType

class Query (object):
    all_inventario = DjangoFilterConnectionField(InventarioType, orderBy=graphene.List(of_type=graphene.String))

    def resolve_all_inventario(self, info, **kwargs):
        orderBy = kwargs.get('orderBy', None)
        if orderBy is None:
          return Inventario.objects.all()
        else:        
          return Inventario.objects.order_by(*orderBy)