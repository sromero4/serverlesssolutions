import graphene
from graphene_django.filter import DjangoFilterConnectionField

from sss_backend.models.conjunto import Propietario, PropietarioType

class Query (object):
    all_propietario = DjangoFilterConnectionField(PropietarioType, orderBy=graphene.List(of_type=graphene.String))

    def resolve_all_propietario(self, info, **kwargs):
        orderBy = kwargs.get('orderBy', None)
        if orderBy is None:
          return Propietario.objects.all()
        else:        
          return Propietario.objects.order_by(*orderBy)