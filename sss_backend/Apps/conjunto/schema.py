import graphene

from .apartamento import schema as apartamento
from .habitante import schema as habitante
from .perfil import schema as perfil
from .persona import schema as persona
from .propietario import schema as propietario
from .torre import schema as torre
from .usuario import schema as usuario

class Query(apartamento.Query, habitante.Query, perfil.Query, persona.Query, propietario.Query, torre.Query, usuario.Query, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    pass    