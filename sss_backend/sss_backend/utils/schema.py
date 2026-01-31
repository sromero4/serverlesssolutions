import graphene
from graphene_django.types import DjangoObjectType
from Apps.conjunto import schema as conjunto
# from Apps.restaurant import schema as restaurant

class ConjQuery(conjunto.Query, graphene.ObjectType):
    pass

# class ConjMutation(graphene.ObjectType):
#     pass

# class RestQuery(restaurant.Query, graphene.ObjectType):
#     pass

schema_conjunto = graphene.Schema(query=ConjQuery)
# schema_restaurant = graphene.Schema(query=RestQuery)
