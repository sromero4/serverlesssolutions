import graphene
from graphene_django.filter import DjangoFilterConnectionField

from sss_backend.models.conjunto import Habitante, HabitanteType

class Query (object):
    all_habitante = DjangoFilterConnectionField(HabitanteType, orderBy=graphene.List(of_type=graphene.String))

    def resolve_all_habitante(self, info, **kwargs):
        orderBy = kwargs.get('orderBy', None)
        if orderBy is None:
          return Habitante.objects.all()
        else:        
          return Habitante.objects.order_by(*orderBy)