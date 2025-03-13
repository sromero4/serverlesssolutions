from django.db import models
from graphene import relay
from graphene_django import DjangoObjectType

from .propietario import *

class PropietarioType(DjangoObjectType):
    class Meta:
        model = Propietario
        interfaces = (relay.Node,)
        app_label = 'conjunto'
        filter_fields = {
                        "prop_codigo":["exact"]
                        }