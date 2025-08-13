import graphene
from graphene_django import DjangoObjectType
from sss_backend.models.restaurant import Inventario
from datetime import datetime

class CreateInventario(graphene.Mutation):
    class Arguments:
        inv_fechahora = graphene.DateTime(required=True)
        usu_codigo = graphene.Int(required=True)

    inventario = graphene.Field('sss_backend.models.restaurant.inventarioType.InventarioType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, inv_fechahora, usu_codigo):
        try:
            inventario = Inventario.objects.create(
                inv_fechahora=inv_fechahora,
                usu_codigo_id=usu_codigo
            )
            return CreateInventario(inventario=inventario, success=True, error=None)
        except Exception as e:
            return CreateInventario(inventario=None, success=False, error=str(e))

class UpdateInventario(graphene.Mutation):
    class Arguments:
        inv_codigo = graphene.Int(required=True)
        inv_fechahora = graphene.DateTime(required=False)
        usu_codigo = graphene.Int(required=False)

    inventario = graphene.Field('sss_backend.models.restaurant.inventarioType.InventarioType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, inv_codigo, **kwargs):
        try:
            inventario = Inventario.objects.get(inv_codigo=inv_codigo)
            
            if 'inv_fechahora' in kwargs:
                inventario.inv_fechahora = kwargs['inv_fechahora']
            if 'usu_codigo' in kwargs:
                inventario.usu_codigo_id = kwargs['usu_codigo']
            
            inventario.save()
            return UpdateInventario(inventario=inventario, success=True, error=None)
        except Inventario.DoesNotExist:
            return UpdateInventario(inventario=None, success=False, error="Inventario no encontrado")
        except Exception as e:
            return UpdateInventario(inventario=None, success=False, error=str(e))

class DeleteInventario(graphene.Mutation):
    class Arguments:
        inv_codigo = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, inv_codigo):
        try:
            inventario = Inventario.objects.get(inv_codigo=inv_codigo)
            inventario.delete()
            return DeleteInventario(success=True, error=None)
        except Inventario.DoesNotExist:
            return DeleteInventario(success=False, error="Inventario no encontrado")
        except Exception as e:
            return DeleteInventario(success=False, error=str(e))

class Mutation(graphene.ObjectType):
    create_inventario = CreateInventario.Field()
    update_inventario = UpdateInventario.Field()
    delete_inventario = DeleteInventario.Field()
