from django.db import models
from graphene import relay
from graphene_django import DjangoObjectType

from .habitante import *

class HabitanteType(DjangoObjectType):
    class Meta:
        model = Habitante
        interfaces = (relay.Node,)
        app_label = 'conjunto'
        filter_fields = {
                        "hab_codigo":["exact"]
                        }