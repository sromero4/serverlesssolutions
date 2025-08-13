import graphene
from graphene_django import DjangoObjectType
from sss_backend.models.restaurant import Inventarioingrediente
from datetime import datetime

class CreateInventarioingrediente(graphene.Mutation):
    class Arguments:
        usu_codigo = graphene.Int(required=True)
        inv_codigo = graphene.Int(required=True)
        ing_codigo = graphene.Int(required=True)

    inventarioingrediente = graphene.Field('sss_backend.models.restaurant.inventarioingredienteType.InventarioingredienteType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, usu_codigo, inv_codigo, ing_codigo):
        try:
            inventarioingrediente = Inventarioingrediente.objects.create(
                usu_codigo_id=usu_codigo,
                inv_codigo_id=inv_codigo,
                ing_codigo_id=ing_codigo,
                inving_fechacreacion=datetime.now()
            )
            return CreateInventarioingrediente(inventarioingrediente=inventarioingrediente, success=True, error=None)
        except Exception as e:
            return CreateInventarioingrediente(inventarioingrediente=None, success=False, error=str(e))

class UpdateInventarioingrediente(graphene.Mutation):
    class Arguments:
        inving_codigo = graphene.Int(required=True)
        usu_codigo = graphene.Int(required=False)
        inv_codigo = graphene.Int(required=False)
        ing_codigo = graphene.Int(required=False)

    inventarioingrediente = graphene.Field('sss_backend.models.restaurant.inventarioingredienteType.InventarioingredienteType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, inving_codigo, **kwargs):
        try:
            inventarioingrediente = Inventarioingrediente.objects.get(inving_codigo=inving_codigo)
            
            if 'usu_codigo' in kwargs:
                inventarioingrediente.usu_codigo_id = kwargs['usu_codigo']
            if 'inv_codigo' in kwargs:
                inventarioingrediente.inv_codigo_id = kwargs['inv_codigo']
            if 'ing_codigo' in kwargs:
                inventarioingrediente.ing_codigo_id = kwargs['ing_codigo']
            
            inventarioingrediente.save()
            return UpdateInventarioingrediente(inventarioingrediente=inventarioingrediente, success=True, error=None)
        except Inventarioingrediente.DoesNotExist:
            return UpdateInventarioingrediente(inventarioingrediente=None, success=False, error="Inventario ingrediente no encontrado")
        except Exception as e:
            return UpdateInventarioingrediente(inventarioingrediente=None, success=False, error=str(e))

class DeleteInventarioingrediente(graphene.Mutation):
    class Arguments:
        inving_codigo = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, inving_codigo):
        try:
            inventarioingrediente = Inventarioingrediente.objects.get(inving_codigo=inving_codigo)
            inventarioingrediente.delete()
            return DeleteInventarioingrediente(success=True, error=None)
        except Inventarioingrediente.DoesNotExist:
            return DeleteInventarioingrediente(success=False, error="Inventario ingrediente no encontrado")
        except Exception as e:
            return DeleteInventarioingrediente(success=False, error=str(e))

class Mutation(graphene.ObjectType):
    create_inventarioingrediente = CreateInventarioingrediente.Field()
    update_inventarioingrediente = UpdateInventarioingrediente.Field()
    delete_inventarioingrediente = DeleteInventarioingrediente.Field()
