import graphene

from .apartamento import schema as apartamento

class Query(apartamento.Query, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    pass    