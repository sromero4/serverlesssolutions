import graphene
from graphene_django import DjangoObjectType
from sss_backend.models.restaurant import Pedidoproducto

class CreatePedidoproducto(graphene.Mutation):
    class Arguments:
        ped_codigo = graphene.Int(required=True)
        prod_codigo = graphene.Int(required=True)

    pedidoproducto = graphene.Field('sss_backend.models.restaurant.pedidoproductoType.PedidoproductoType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, ped_codigo, prod_codigo):
        try:
            pedidoproducto = Pedidoproducto.objects.create(
                ped_codigo_id=ped_codigo,
                prod_codigo_id=prod_codigo
            )
            return CreatePedidoproducto(pedidoproducto=pedidoproducto, success=True, error=None)
        except Exception as e:
            return CreatePedidoproducto(pedidoproducto=None, success=False, error=str(e))

class UpdatePedidoproducto(graphene.Mutation):
    class Arguments:
        pedprod_codigo = graphene.Int(required=True)
        ped_codigo = graphene.Int(required=False)
        prod_codigo = graphene.Int(required=False)

    pedidoproducto = graphene.Field('sss_backend.models.restaurant.pedidoproductoType.PedidoproductoType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, pedprod_codigo, **kwargs):
        try:
            pedidoproducto = Pedidoproducto.objects.get(pedprod_codigo=pedprod_codigo)
            
            if 'ped_codigo' in kwargs:
                pedidoproducto.ped_codigo_id = kwargs['ped_codigo']
            if 'prod_codigo' in kwargs:
                pedidoproducto.prod_codigo_id = kwargs['prod_codigo']
            
            pedidoproducto.save()
            return UpdatePedidoproducto(pedidoproducto=pedidoproducto, success=True, error=None)
        except Pedidoproducto.DoesNotExist:
            return UpdatePedidoproducto(pedidoproducto=None, success=False, error="Pedido producto no encontrado")
        except Exception as e:
            return UpdatePedidoproducto(pedidoproducto=None, success=False, error=str(e))

class DeletePedidoproducto(graphene.Mutation):
    class Arguments:
        pedprod_codigo = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, pedprod_codigo):
        try:
            pedidoproducto = Pedidoproducto.objects.get(pedprod_codigo=pedprod_codigo)
            pedidoproducto.delete()
            return DeletePedidoproducto(success=True, error=None)
        except Pedidoproducto.DoesNotExist:
            return DeletePedidoproducto(success=False, error="Pedido producto no encontrado")
        except Exception as e:
            return DeletePedidoproducto(success=False, error=str(e))

class Mutation(graphene.ObjectType):
    create_pedidoproducto = CreatePedidoproducto.Field()
    update_pedidoproducto = UpdatePedidoproducto.Field()
    delete_pedidoproducto = DeletePedidoproducto.Field()
