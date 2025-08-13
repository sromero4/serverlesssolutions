from django.db import models
from graphene import relay
from graphene_django import DjangoObjectType

from .perfil import *

class PerfilType(DjangoObjectType):
    class Meta:
        model = Perfil
        interfaces = (relay.Node,)
        app_label = 'restaurant'
        filter_fields = {
                        "per_codigo":["exact"],
                        }
