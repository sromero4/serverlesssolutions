from django.db import models
from graphene import relay
from graphene_django import DjangoObjectType

from .jornada import *

class JornadaType(DjangoObjectType):
    class Meta:
        model = Jornada
        interfaces = (relay.Node,)
        app_label = 'restaurant'
        filter_fields = {
                        "jor_codigo":["exact"],
                        }
