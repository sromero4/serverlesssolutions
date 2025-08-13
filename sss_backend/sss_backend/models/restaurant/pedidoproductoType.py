from django.db import models
from graphene import relay
from graphene_django import DjangoObjectType

from .pedidoproducto import *

class PedidoproductoType(DjangoObjectType):
    class Meta:
        model = Pedidoproducto
        interfaces = (relay.Node,)
        app_label = 'restaurant'
        filter_fields = {
                        "pedprod_codigo":["exact"],
                        }
