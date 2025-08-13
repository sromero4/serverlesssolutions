import graphene
from graphene_django import DjangoObjectType
from sss_backend.models.restaurant import Ingrediente
from datetime import datetime

class CreateIngrediente(graphene.Mutation):
    class Arguments:
        ing_nombre = graphene.String(required=True)
        ing_cantidad = graphene.Decimal(required=True)
        usu_codigo = graphene.Int(required=True)
        tipprod_codigo = graphene.Int(required=True)
        tipcant_codigo = graphene.Int(required=True)

    ingrediente = graphene.Field('sss_backend.models.restaurant.ingredienteType.IngredienteType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, ing_nombre, ing_cantidad, usu_codigo, tipprod_codigo, tipcant_codigo):
        try:
            ingrediente = Ingrediente.objects.create(
                ing_nombre=ing_nombre,
                ing_cantidad=ing_cantidad,
                usu_codigo_id=usu_codigo,
                tipprod_codigo_id=tipprod_codigo,
                tipcant_codigo_id=tipcant_codigo,
                ing_fechacreacion=datetime.now()
            )
            return CreateIngrediente(ingrediente=ingrediente, success=True, error=None)
        except Exception as e:
            return CreateIngrediente(ingrediente=None, success=False, error=str(e))

class UpdateIngrediente(graphene.Mutation):
    class Arguments:
        ing_codigo = graphene.Int(required=True)
        ing_nombre = graphene.String(required=False)
        ing_cantidad = graphene.Decimal(required=False)
        usu_codigo = graphene.Int(required=False)
        tipprod_codigo = graphene.Int(required=False)
        tipcant_codigo = graphene.Int(required=False)

    ingrediente = graphene.Field('sss_backend.models.restaurant.ingredienteType.IngredienteType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, ing_codigo, **kwargs):
        try:
            ingrediente = Ingrediente.objects.get(ing_codigo=ing_codigo)
            
            if 'ing_nombre' in kwargs:
                ingrediente.ing_nombre = kwargs['ing_nombre']
            if 'ing_cantidad' in kwargs:
                ingrediente.ing_cantidad = kwargs['ing_cantidad']
            if 'usu_codigo' in kwargs:
                ingrediente.usu_codigo_id = kwargs['usu_codigo']
            if 'tipprod_codigo' in kwargs:
                ingrediente.tipprod_codigo_id = kwargs['tipprod_codigo']
            if 'tipcant_codigo' in kwargs:
                ingrediente.tipcant_codigo_id = kwargs['tipcant_codigo']
            
            ingrediente.save()
            return UpdateIngrediente(ingrediente=ingrediente, success=True, error=None)
        except Ingrediente.DoesNotExist:
            return UpdateIngrediente(ingrediente=None, success=False, error="Ingrediente no encontrado")
        except Exception as e:
            return UpdateIngrediente(ingrediente=None, success=False, error=str(e))

class DeleteIngrediente(graphene.Mutation):
    class Arguments:
        ing_codigo = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, ing_codigo):
        try:
            ingrediente = Ingrediente.objects.get(ing_codigo=ing_codigo)
            ingrediente.delete()
            return DeleteIngrediente(success=True, error=None)
        except Ingrediente.DoesNotExist:
            return DeleteIngrediente(success=False, error="Ingrediente no encontrado")
        except Exception as e:
            return DeleteIngrediente(success=False, error=str(e))

class Mutation(graphene.ObjectType):
    create_ingrediente = CreateIngrediente.Field()
    update_ingrediente = UpdateIngrediente.Field()
    delete_ingrediente = DeleteIngrediente.Field()
