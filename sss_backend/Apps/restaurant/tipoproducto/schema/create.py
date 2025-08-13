import graphene
from graphene_django import DjangoObjectType
from sss_backend.models.restaurant import Tipoproducto

class CreateTipoproducto(graphene.Mutation):
    class Arguments:
        tipprod_nombre = graphene.String(required=True)

    tipoproducto = graphene.Field('sss_backend.models.restaurant.tipoproductoType.TipoproductoType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, tipprod_nombre):
        try:
            tipoproducto = Tipoproducto.objects.create(
                tipprod_nombre=tipprod_nombre
            )
            return CreateTipoproducto(tipoproducto=tipoproducto, success=True, error=None)
        except Exception as e:
            return CreateTipoproducto(tipoproducto=None, success=False, error=str(e))

class UpdateTipoproducto(graphene.Mutation):
    class Arguments:
        tipprod_codigo = graphene.Int(required=True)
        tipprod_nombre = graphene.String(required=False)

    tipoproducto = graphene.Field('sss_backend.models.restaurant.tipoproductoType.TipoproductoType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, tipprod_codigo, **kwargs):
        try:
            tipoproducto = Tipoproducto.objects.get(tipprod_codigo=tipprod_codigo)
            
            if 'tipprod_nombre' in kwargs:
                tipoproducto.tipprod_nombre = kwargs['tipprod_nombre']
            
            tipoproducto.save()
            return UpdateTipoproducto(tipoproducto=tipoproducto, success=True, error=None)
        except Tipoproducto.DoesNotExist:
            return UpdateTipoproducto(tipoproducto=None, success=False, error="Tipo producto no encontrado")
        except Exception as e:
            return UpdateTipoproducto(tipoproducto=None, success=False, error=str(e))

class DeleteTipoproducto(graphene.Mutation):
    class Arguments:
        tipprod_codigo = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, tipprod_codigo):
        try:
            tipoproducto = Tipoproducto.objects.get(tipprod_codigo=tipprod_codigo)
            tipoproducto.delete()
            return DeleteTipoproducto(success=True, error=None)
        except Tipoproducto.DoesNotExist:
            return DeleteTipoproducto(success=False, error="Tipo producto no encontrado")
        except Exception as e:
            return DeleteTipoproducto(success=False, error=str(e))

class Mutation(graphene.ObjectType):
    create_tipoproducto = CreateTipoproducto.Field()
    update_tipoproducto = UpdateTipoproducto.Field()
    delete_tipoproducto = DeleteTipoproducto.Field()
