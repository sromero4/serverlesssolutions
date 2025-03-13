import graphene
from graphene_django.filter import DjangoFilterConnectionField

from sss_backend.models.conjunto import Torre, TorreType

class Query (object):
    all_torre = DjangoFilterConnectionField(TorreType, orderBy=graphene.List(of_type=graphene.String))

    def resolve_all_torre(self, info, **kwargs):
        orderBy = kwargs.get('orderBy', None)
        if orderBy is None:
          return Torre.objects.all()
        else:        
          return Torre.objects.order_by(*orderBy)