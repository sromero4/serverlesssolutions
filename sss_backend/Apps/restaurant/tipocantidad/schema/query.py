import graphene
from graphene_django.filter import DjangoFilterConnectionField

from sss_backend.models.restaurant import Tipocantidad, TipocantidadType

class Query (object):
    all_tipocantidad = DjangoFilterConnectionField(TipocantidadType, orderBy=graphene.List(of_type=graphene.String))

    def resolve_all_tipocantidad(self, info, **kwargs):
        orderBy = kwargs.get('orderBy', None)
        if orderBy is None:
          return Tipocantidad.objects.all()
        else:        
          return Tipocantidad.objects.order_by(*orderBy)