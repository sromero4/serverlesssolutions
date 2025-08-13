import graphene
from graphene_django.filter import DjangoFilterConnectionField

from sss_backend.models.restaurant import Inventarioingrediente, InventarioingredienteType

class Query (object):
    all_inventarioingrediente = DjangoFilterConnectionField(InventarioingredienteType, orderBy=graphene.List(of_type=graphene.String))

    def resolve_all_inventarioingrediente(self, info, **kwargs):
        orderBy = kwargs.get('orderBy', None)
        if orderBy is None:
          return Inventarioingrediente.objects.all()
        else:        
          return Inventarioingrediente.objects.order_by(*orderBy)