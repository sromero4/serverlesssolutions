from django.db import models
from graphene import relay
from graphene_django import DjangoObjectType

from .producto import *

class ProductoType(DjangoObjectType):
    class Meta:
        model = Producto
        interfaces = (relay.Node,)
        app_label = 'restaurant'
        filter_fields = {
                        "prod_codigo":["exact"],
                        "prod_nombre":["exact", "icontains"],
                        }
