import graphene
from graphene_django import DjangoObjectType
from sss_backend.models.restaurant import Estado

class CreateEstado(graphene.Mutation):
    class Arguments:
        est_nombre = graphene.String(required=True)

    estado = graphene.Field('sss_backend.models.restaurant.estadoType.EstadoType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, est_nombre):
        try:
            estado = Estado.objects.create(est_nombre=est_nombre)
            return CreateEstado(estado=estado, success=True, error=None)
        except Exception as e:
            return CreateEstado(estado=None, success=False, error=str(e))

class UpdateEstado(graphene.Mutation):
    class Arguments:
        est_codigo = graphene.Int(required=True)
        est_nombre = graphene.String(required=True)

    estado = graphene.Field('sss_backend.models.restaurant.estadoType.EstadoType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, est_codigo, est_nombre):
        try:
            estado = Estado.objects.get(est_codigo=est_codigo)
            estado.est_nombre = est_nombre
            estado.save()
            return UpdateEstado(estado=estado, success=True, error=None)
        except Estado.DoesNotExist:
            return UpdateEstado(estado=None, success=False, error="Estado no encontrado")
        except Exception as e:
            return UpdateEstado(estado=None, success=False, error=str(e))

class DeleteEstado(graphene.Mutation):
    class Arguments:
        est_codigo = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, est_codigo):
        try:
            estado = Estado.objects.get(est_codigo=est_codigo)
            estado.delete()
            return DeleteEstado(success=True, error=None)
        except Estado.DoesNotExist:
            return DeleteEstado(success=False, error="Estado no encontrado")
        except Exception as e:
            return DeleteEstado(success=False, error=str(e))

class Mutation(graphene.ObjectType):
    create_estado = CreateEstado.Field()
    update_estado = UpdateEstado.Field()
    delete_estado = DeleteEstado.Field()
