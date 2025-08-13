import graphene
from graphene_django.filter import DjangoFilterConnectionField

from sss_backend.models.restaurant import Ingrediente, IngredienteType

class Query (object):
    all_ingrediente = DjangoFilterConnectionField(IngredienteType, orderBy=graphene.List(of_type=graphene.String))

    def resolve_all_ingrediente(self, info, **kwargs):
        orderBy = kwargs.get('orderBy', None)
        if orderBy is None:
          return Ingrediente.objects.all()
        else:        
          return Ingrediente.objects.order_by(*orderBy)