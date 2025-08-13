from django.db import models
from graphene import relay
from graphene_django import DjangoObjectType

from .tipocantidad import *

class TipocantidadType(DjangoObjectType):
    class Meta:
        model = Tipocantidad
        interfaces = (relay.Node,)
        app_label = 'restaurant'
        filter_fields = {
                        "tipcant_codigo":["exact"],
                        "tipcant_nombre":["exact", "icontains"]
                        }
