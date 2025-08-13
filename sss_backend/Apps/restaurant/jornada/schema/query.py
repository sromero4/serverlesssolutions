import graphene
from graphene_django.filter import DjangoFilterConnectionField

from sss_backend.models.restaurant import Jornada, JornadaType

class Query (object):
    all_jornada = DjangoFilterConnectionField(JornadaType, orderBy=graphene.List(of_type=graphene.String))

    def resolve_all_jornada(self, info, **kwargs):
        orderBy = kwargs.get('orderBy', None)
        if orderBy is None:
          return Jornada.objects.all()
        else:        
          return Jornada.objects.order_by(*orderBy)