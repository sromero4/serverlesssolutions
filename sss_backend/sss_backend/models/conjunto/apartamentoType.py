from django.db import models
from graphene import relay
from graphene_django import DjangoObjectType

from .apartamento import *

class ApartamentoType(DjangoObjectType):
    class Meta:
        model = Apartamento
        interfaces = (relay.Node,)
        app_label = 'conjunto'
        filter_fields = {
                        "apto_codigo":["exact"]
                        }