import graphene
from graphene_django.filter import DjangoFilterConnectionField

from sss_backend.models.conjunto import Apartamento, ApartamentoType

class Query (object):
    all_apartamento = DjangoFilterConnectionField(ApartamentoType, orderBy=graphene.List(of_type=graphene.String))

    def resolve_all_apartamento(self, info, **kwargs):
        orderBy = kwargs.get('orderBy', None)
        if orderBy is None:
          return Apartamento.objects.all()
        else:        
          return Apartamento.objects.order_by(*orderBy)