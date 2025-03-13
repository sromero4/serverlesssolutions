from django.db import models
from graphene import relay
from graphene_django import DjangoObjectType

from .usuario import *

class UsuarioType(DjangoObjectType):
    class Meta:
        model = Usuario
        interfaces = (relay.Node,)
        app_label = 'conjunto'
        filter_fields = {
                        "usu_codigo":["exact"]
                        }