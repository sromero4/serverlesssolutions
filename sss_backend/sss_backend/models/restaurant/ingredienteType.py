from django.db import models
from graphene import relay
from graphene_django import DjangoObjectType

from .ingrediente import *

class IngredienteType(DjangoObjectType):
    class Meta:
        model = Ingrediente
        interfaces = (relay.Node,)
        app_label = 'restaurant'
        filter_fields = {
                        "ing_codigo":["exact"],
                        "ing_nombre":["exact", "icontains"],
                        }
