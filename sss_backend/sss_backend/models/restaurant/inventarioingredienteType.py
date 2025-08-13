from django.db import models
from graphene import relay
from graphene_django import DjangoObjectType

from .inventarioingrediente import *

class InventarioingredienteType(DjangoObjectType):
    class Meta:
        model = Inventarioingrediente
        interfaces = (relay.Node,)
        app_label = 'restaurant'
        filter_fields = {
                        "inving_codigo":["exact"],
                        }
