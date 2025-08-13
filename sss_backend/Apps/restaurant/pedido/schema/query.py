import graphene
from graphene_django.filter import DjangoFilterConnectionField

from sss_backend.models.restaurant import Pedido, PedidoType

class Query (object):
    all_pedido = DjangoFilterConnectionField(PedidoType, orderBy=graphene.List(of_type=graphene.String))

    def resolve_all_pedido(self, info, **kwargs):
        orderBy = kwargs.get('orderBy', None)
        if orderBy is None:
          return Pedido.objects.all()
        else:        
          return Pedido.objects.order_by(*orderBy)