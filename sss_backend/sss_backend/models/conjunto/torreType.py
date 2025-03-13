from django.db import models
from graphene import relay
from graphene_django import DjangoObjectType

from .torre import *

class TorreType(DjangoObjectType):
    class Meta:
        model = Torre
        interfaces = (relay.Node,)
        app_label = 'conjunto'
        filter_fields = {
                        "tor_codigo":["exact"]
                        }