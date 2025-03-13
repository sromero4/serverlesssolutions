import graphene
from graphene_django.filter import DjangoFilterConnectionField

from sss_backend.models.conjunto import Usuario, UsuarioType

class Query (object):
    all_usuario = DjangoFilterConnectionField(UsuarioType, orderBy=graphene.List(of_type=graphene.String))

    def resolve_all_usuario(self, info, **kwargs):
        orderBy = kwargs.get('orderBy', None)
        if orderBy is None:
          return Usuario.objects.all()
        else:        
          return Usuario.objects.order_by(*orderBy)