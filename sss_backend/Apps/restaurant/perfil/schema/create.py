import graphene
from graphene_django import DjangoObjectType
from sss_backend.models.restaurant import Perfil
from datetime import datetime

class CreatePerfil(graphene.Mutation):
    class Arguments:
        per_nombre = graphene.String(required=True)
        est_codigo = graphene.Int(required=True)

    perfil = graphene.Field('sss_backend.models.restaurant.perfilType.PerfilType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, per_nombre, est_codigo):
        try:
            perfil = Perfil.objects.create(
                per_nombre=per_nombre,
                est_codigo_id=est_codigo,
                per_fechacreacion=datetime.now()
            )
            return CreatePerfil(perfil=perfil, success=True, error=None)
        except Exception as e:
            return CreatePerfil(perfil=None, success=False, error=str(e))

class UpdatePerfil(graphene.Mutation):
    class Arguments:
        per_codigo = graphene.Int(required=True)
        per_nombre = graphene.String(required=False)
        est_codigo = graphene.Int(required=False)

    perfil = graphene.Field('sss_backend.models.restaurant.perfilType.PerfilType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, per_codigo, **kwargs):
        try:
            perfil = Perfil.objects.get(per_codigo=per_codigo)
            
            if 'per_nombre' in kwargs:
                perfil.per_nombre = kwargs['per_nombre']
            if 'est_codigo' in kwargs:
                perfil.est_codigo_id = kwargs['est_codigo']
            
            perfil.save()
            return UpdatePerfil(perfil=perfil, success=True, error=None)
        except Perfil.DoesNotExist:
            return UpdatePerfil(perfil=None, success=False, error="Perfil no encontrado")
        except Exception as e:
            return UpdatePerfil(perfil=None, success=False, error=str(e))

class DeletePerfil(graphene.Mutation):
    class Arguments:
        per_codigo = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, per_codigo):
        try:
            perfil = Perfil.objects.get(per_codigo=per_codigo)
            perfil.delete()
            return DeletePerfil(success=True, error=None)
        except Perfil.DoesNotExist:
            return DeletePerfil(success=False, error="Perfil no encontrado")
        except Exception as e:
            return DeletePerfil(success=False, error=str(e))

class Mutation(graphene.ObjectType):
    create_perfil = CreatePerfil.Field()
    update_perfil = UpdatePerfil.Field()
    delete_perfil = DeletePerfil.Field()
