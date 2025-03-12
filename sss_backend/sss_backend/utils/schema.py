import graphene
from graphene_django.types import DjangoObjectType
# from Apps.conjunto import schema as conjunto

class ConjQuery(graphene.ObjectType):
    pass

class ConjMutation(graphene.ObjectType):
    pass

schema_conjunto = graphene.Schema(query=ConjQuery, mutation=ConjMutation)
