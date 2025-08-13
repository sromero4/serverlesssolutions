import graphene
from graphene_django.filter import DjangoFilterConnectionField

from sss_backend.models.restaurant import Estado, EstadoType

class Query (object):
    all_estado = DjangoFilterConnectionField(EstadoType, orderBy=graphene.List(of_type=graphene.String))

    def resolve_all_estado(self, info, **kwargs):
        orderBy = kwargs.get('orderBy', None)
        if orderBy is None:
          return Estado.objects.all()
        else:        
          return Estado.objects.order_by(*orderBy)