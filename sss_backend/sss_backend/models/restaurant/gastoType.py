from django.db import models
from graphene import relay
from graphene_django import DjangoObjectType

from .gasto import *

class GastoType(DjangoObjectType):
    class Meta:
        model = Gasto
        interfaces = (relay.Node,)
        app_label = 'restaurant'
        filter_fields = {
                        "gas_codigo":["exact"],
                        }
