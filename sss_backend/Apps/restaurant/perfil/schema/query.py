import graphene
from graphene_django.filter import DjangoFilterConnectionField

from sss_backend.models.restaurant import Perfil, PerfilType

class Query (object):
    all_perfil = DjangoFilterConnectionField(PerfilType, orderBy=graphene.List(of_type=graphene.String))

    def resolve_all_perfil(self, info, **kwargs):
        orderBy = kwargs.get('orderBy', None)
        if orderBy is None:
          return Perfil.objects.all()
        else:        
          return Perfil.objects.order_by(*orderBy)