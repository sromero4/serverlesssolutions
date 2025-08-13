import graphene
from .estado import schema as estado
from .gasto import schema as gasto
from .ingrediente import schema as ingrediente
from .inventario import schema as inventario
from .inventarioingrediente import schema as inventarioingrediente
from .jornada import schema as jornada
from .pedido import schema as pedido
from .pedidoproducto import schema as pedidoproducto
from .perfil import schema as perfil
from .producto import schema as producto
from .tipocantidad import schema as tipocantidad
from .tipoproducto import schema as tipoproducto
from .usuario import schema as usuario

class Query(estado.Query, gasto.Query, ingrediente.Query, inventario.Query, inventarioingrediente.Query, jornada.Query, pedido.Query, pedidoproducto.Query, perfil.Query, producto.Query, tipocantidad.Query, tipoproducto.Query, usuario.Query, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    pass    