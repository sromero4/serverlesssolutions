import graphene
from graphene_django.filter import DjangoFilterConnectionField

from sss_backend.models.restaurant import Gasto, GastoType

class Query (object):
    all_gasto = DjangoFilterConnectionField(GastoType, orderBy=graphene.List(of_type=graphene.String))

    def resolve_all_gasto(self, info, **kwargs):
        orderBy = kwargs.get('orderBy', None)
        if orderBy is None:
          return Gasto.objects.all()
        else:        
          return Gasto.objects.order_by(*orderBy)