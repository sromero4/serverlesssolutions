from django.db import models
from graphene import relay
from graphene_django import DjangoObjectType

from .usuario import *

class UsuarioType(DjangoObjectType):
    class Meta:
        model = Usuario
        interfaces = (relay.Node,)
        app_label = 'restaurant'
        filter_fields = {
                        "usu_codigo":["exact"],
                        "usu_nombre":["exact", "icontains"],
                        "usu_apellido":["exact", "icontains"],
                        "est_codigo":["exact"],
                        "per_codigo":["exact"]
                        }
