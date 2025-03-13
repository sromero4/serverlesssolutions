from django.db import models
from graphene import relay
from graphene_django import DjangoObjectType

from .persona import *

class PersonaType(DjangoObjectType):
    class Meta:
        model = Persona
        interfaces = (relay.Node,)
        app_label = 'conjunto'
        filter_fields = {
                        "per_codigo":["exact"]
                        }