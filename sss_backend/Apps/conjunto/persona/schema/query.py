import graphene
from graphene_django.filter import DjangoFilterConnectionField

from sss_backend.models.conjunto import Persona, PersonaType

class Query (object):
    all_persona = DjangoFilterConnectionField(PersonaType, orderBy=graphene.List(of_type=graphene.String))

    def resolve_all_persona(self, info, **kwargs):
        orderBy = kwargs.get('orderBy', None)
        if orderBy is None:
          return Persona.objects.all()
        else:        
          return Persona.objects.order_by(*orderBy)