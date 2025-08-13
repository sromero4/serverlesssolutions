import graphene
from graphene_django import DjangoObjectType
from sss_backend.models.restaurant import Usuario
from datetime import datetime

class CreateUsuario(graphene.Mutation):
    class Arguments:
        usu_nombre = graphene.String(required=True)
        usu_login = graphene.String(required=True)
        usu_clave = graphene.String(required=True)
        usu_telefono = graphene.String(required=False)
        usu_apellido = graphene.String(required=False)
        est_codigo = graphene.Int(required=True)
        per_codigo = graphene.Int(required=True)

    usuario = graphene.Field('sss_backend.models.restaurant.usuarioType.UsuarioType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, usu_nombre, usu_login, usu_clave, est_codigo, per_codigo, usu_telefono=None, usu_apellido=None):
        try:
            usuario = Usuario.objects.create(
                usu_nombre=usu_nombre,
                usu_login=usu_login,
                usu_clave=usu_clave,
                usu_telefono=usu_telefono,
                usu_apellido=usu_apellido,
                est_codigo_id=est_codigo,
                per_codigo_id=per_codigo,
                usu_fechacreacion=datetime.now()
            )
            return CreateUsuario(usuario=usuario, success=True, error=None)
        except Exception as e:
            return CreateUsuario(usuario=None, success=False, error=str(e))

class UpdateUsuario(graphene.Mutation):
    class Arguments:
        usu_codigo = graphene.Int(required=True)
        usu_nombre = graphene.String(required=False)
        usu_telefono = graphene.String(required=False)
        usu_login = graphene.String(required=False)
        usu_clave = graphene.String(required=False)
        usu_apellido = graphene.String(required=False)
        est_codigo = graphene.Int(required=False)
        per_codigo = graphene.Int(required=False)

    usuario = graphene.Field('sss_backend.models.restaurant.usuarioType.UsuarioType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, usu_codigo, **kwargs):
        try:
            usuario = Usuario.objects.get(usu_codigo=usu_codigo)
            
            if 'usu_nombre' in kwargs:
                usuario.usu_nombre = kwargs['usu_nombre']
            if 'usu_telefono' in kwargs:
                usuario.usu_telefono = kwargs['usu_telefono']
            if 'usu_login' in kwargs:
                usuario.usu_login = kwargs['usu_login']
            if 'usu_clave' in kwargs:
                usuario.usu_clave = kwargs['usu_clave']
            if 'usu_apellido' in kwargs:
                usuario.usu_apellido = kwargs['usu_apellido']
            if 'est_codigo' in kwargs:
                usuario.est_codigo_id = kwargs['est_codigo']
            if 'per_codigo' in kwargs:
                usuario.per_codigo_id = kwargs['per_codigo']
            
            usuario.usu_fechamodificacion = datetime.now()
            usuario.save()
            return UpdateUsuario(usuario=usuario, success=True, error=None)
        except Usuario.DoesNotExist:
            return UpdateUsuario(usuario=None, success=False, error="Usuario no encontrado")
        except Exception as e:
            return UpdateUsuario(usuario=None, success=False, error=str(e))

class DeleteUsuario(graphene.Mutation):
    class Arguments:
        usu_codigo = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, usu_codigo):
        try:
            usuario = Usuario.objects.get(usu_codigo=usu_codigo)
            usuario.delete()
            return DeleteUsuario(success=True, error=None)
        except Usuario.DoesNotExist:
            return DeleteUsuario(success=False, error="Usuario no encontrado")
        except Exception as e:
            return DeleteUsuario(success=False, error=str(e))

class Mutation(graphene.ObjectType):
    create_usuario = CreateUsuario.Field()
    update_usuario = UpdateUsuario.Field()
    delete_usuario = DeleteUsuario.Field()
