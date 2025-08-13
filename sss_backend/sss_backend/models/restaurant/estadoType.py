from django.db import models
from graphene import relay
from graphene_django import DjangoObjectType

from .estado import *

class EstadoType(DjangoObjectType):
    class Meta:
        model = Estado
        interfaces = (relay.Node,)
        app_label = 'restaurant'
        filter_fields = {
                        "est_codigo":["exact"],
                        "est_nombre":["exact", "icontains"]
                        }
