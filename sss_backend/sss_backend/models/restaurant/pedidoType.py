from django.db import models
from graphene import relay
from graphene_django import DjangoObjectType

from .pedido import *

class PedidoType(DjangoObjectType):
    class Meta:
        model = Pedido
        interfaces = (relay.Node,)
        app_label = 'restaurant'
        filter_fields = {
                        "ped_codigo":["exact"],
                        }
