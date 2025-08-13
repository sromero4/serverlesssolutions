import graphene
from graphene_django import DjangoObjectType
from sss_backend.models.restaurant import Tipocantidad

class CreateTipocantidad(graphene.Mutation):
    class Arguments:
        tipcant_nombre = graphene.String(required=True)

    tipocantidad = graphene.Field('sss_backend.models.restaurant.tipocantidadType.TipocantidadType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, tipcant_nombre):
        try:
            tipocantidad = Tipocantidad.objects.create(
                tipcant_nombre=tipcant_nombre
            )
            return CreateTipocantidad(tipocantidad=tipocantidad, success=True, error=None)
        except Exception as e:
            return CreateTipocantidad(tipocantidad=None, success=False, error=str(e))

class UpdateTipocantidad(graphene.Mutation):
    class Arguments:
        tipcant_codigo = graphene.Int(required=True)
        tipcant_nombre = graphene.String(required=False)

    tipocantidad = graphene.Field('sss_backend.models.restaurant.tipocantidadType.TipocantidadType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, tipcant_codigo, **kwargs):
        try:
            tipocantidad = Tipocantidad.objects.get(tipcant_codigo=tipcant_codigo)
            
            if 'tipcant_nombre' in kwargs:
                tipocantidad.tipcant_nombre = kwargs['tipcant_nombre']
            
            tipocantidad.save()
            return UpdateTipocantidad(tipocantidad=tipocantidad, success=True, error=None)
        except Tipocantidad.DoesNotExist:
            return UpdateTipocantidad(tipocantidad=None, success=False, error="Tipo cantidad no encontrado")
        except Exception as e:
            return UpdateTipocantidad(tipocantidad=None, success=False, error=str(e))

class DeleteTipocantidad(graphene.Mutation):
    class Arguments:
        tipcant_codigo = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, tipcant_codigo):
        try:
            tipocantidad = Tipocantidad.objects.get(tipcant_codigo=tipcant_codigo)
            tipocantidad.delete()
            return DeleteTipocantidad(success=True, error=None)
        except Tipocantidad.DoesNotExist:
            return DeleteTipocantidad(success=False, error="Tipo cantidad no encontrado")
        except Exception as e:
            return DeleteTipocantidad(success=False, error=str(e))

class Mutation(graphene.ObjectType):
    create_tipocantidad = CreateTipocantidad.Field()
    update_tipocantidad = UpdateTipocantidad.Field()
    delete_tipocantidad = DeleteTipocantidad.Field()
