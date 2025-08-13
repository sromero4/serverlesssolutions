import graphene
from graphene_django import DjangoObjectType
from sss_backend.models.restaurant import Gasto
from datetime import datetime

class CreateGasto(graphene.Mutation):
    class Arguments:
        gas_fechacompra = graphene.DateTime(required=True)
        gas_monto = graphene.Decimal(required=True)
        gas_descripcion = graphene.String(required=False)
        gas_observaciones = graphene.String(required=False)
        gas_imagen = graphene.String(required=False)

    gasto = graphene.Field('sss_backend.models.restaurant.gastoType.GastoType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, gas_fechacompra, gas_monto, gas_descripcion=None, gas_observaciones=None, gas_imagen=None):
        try:
            gasto = Gasto.objects.create(
                gas_fechacompra=gas_fechacompra,
                gas_monto=gas_monto,
                gas_descripcion=gas_descripcion,
                gas_observaciones=gas_observaciones,
                gas_imagen=gas_imagen,
                gas_fechacreacion=datetime.now()
            )
            return CreateGasto(gasto=gasto, success=True, error=None)
        except Exception as e:
            return CreateGasto(gasto=None, success=False, error=str(e))

class UpdateGasto(graphene.Mutation):
    class Arguments:
        gas_codigo = graphene.Int(required=True)
        gas_fechacompra = graphene.DateTime(required=False)
        gas_monto = graphene.Decimal(required=False)
        gas_descripcion = graphene.String(required=False)
        gas_observaciones = graphene.String(required=False)
        gas_imagen = graphene.String(required=False)

    gasto = graphene.Field('sss_backend.models.restaurant.gastoType.GastoType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, gas_codigo, **kwargs):
        try:
            gasto = Gasto.objects.get(gas_codigo=gas_codigo)
            
            # Actualizar solo los campos proporcionados
            if 'gas_fechacompra' in kwargs:
                gasto.gas_fechacompra = kwargs['gas_fechacompra']
            if 'gas_monto' in kwargs:
                gasto.gas_monto = kwargs['gas_monto']
            if 'gas_descripcion' in kwargs:
                gasto.gas_descripcion = kwargs['gas_descripcion']
            if 'gas_observaciones' in kwargs:
                gasto.gas_observaciones = kwargs['gas_observaciones']
            if 'gas_imagen' in kwargs:
                gasto.gas_imagen = kwargs['gas_imagen']
            
            gasto.save()
            return UpdateGasto(gasto=gasto, success=True, error=None)
        except Gasto.DoesNotExist:
            return UpdateGasto(gasto=None, success=False, error="Gasto no encontrado")
        except Exception as e:
            return UpdateGasto(gasto=None, success=False, error=str(e))

class DeleteGasto(graphene.Mutation):
    class Arguments:
        gas_codigo = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, gas_codigo):
        try:
            gasto = Gasto.objects.get(gas_codigo=gas_codigo)
            gasto.delete()
            return DeleteGasto(success=True, error=None)
        except Gasto.DoesNotExist:
            return DeleteGasto(success=False, error="Gasto no encontrado")
        except Exception as e:
            return DeleteGasto(success=False, error=str(e))

class Mutation(graphene.ObjectType):
    create_gasto = CreateGasto.Field()
    update_gasto = UpdateGasto.Field()
    delete_gasto = DeleteGasto.Field()
