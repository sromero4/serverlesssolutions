from django.db import models
from graphene import relay
from graphene_django import DjangoObjectType

from .inventario import *

class InventarioType(DjangoObjectType):
    class Meta:
        model = Inventario
        interfaces = (relay.Node,)
        app_label = 'restaurant'
        filter_fields = {
                        "inv_codigo":["exact"],
                        }
