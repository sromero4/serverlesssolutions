import graphene
from graphene_django.filter import DjangoFilterConnectionField

from sss_backend.models.restaurant import Pedidoproducto, PedidoproductoType

class Query (object):
    all_pedidoproducto = DjangoFilterConnectionField(PedidoproductoType, orderBy=graphene.List(of_type=graphene.String))

    def resolve_all_pedidoproducto(self, info, **kwargs):
        orderBy = kwargs.get('orderBy', None)
        if orderBy is None:
          return Pedidoproducto.objects.all()
        else:        
          return Pedidoproducto.objects.order_by(*orderBy)