from django.db import models
from graphene import relay
from graphene_django import DjangoObjectType

from .tipoproducto import *

class TipoproductoType(DjangoObjectType):
    class Meta:
        model = Tipoproducto
        interfaces = (relay.Node,)
        app_label = 'restaurant'
        filter_fields = {
                        "tipprod_codigo":["exact"],
                        "tipprod_nombre":["exact", "icontains"]
                        }
