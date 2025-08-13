import graphene
from graphene_django.filter import DjangoFilterConnectionField

from sss_backend.models.restaurant import Tipoproducto, TipoproductoType

class Query (object):
    all_tipoproducto = DjangoFilterConnectionField(TipoproductoType, orderBy=graphene.List(of_type=graphene.String))

    def resolve_all_tipoproducto(self, info, **kwargs):
        orderBy = kwargs.get('orderBy', None)
        if orderBy is None:
          return Tipoproducto.objects.all()
        else:        
          return Tipoproducto.objects.order_by(*orderBy)