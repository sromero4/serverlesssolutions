import graphene
from graphene_django import DjangoObjectType
from sss_backend.models.restaurant import Jornada
from datetime import datetime

class CreateJornada(graphene.Mutation):
    class Arguments:
        jor_iniciofechahora = graphene.DateTime(required=True)
        jor_finfechahora = graphene.DateTime(required=False)
        jor_pedidototal = graphene.Decimal(required=False)
        jor_ventatotal = graphene.Decimal(required=False)
        usu_codigo = graphene.Int(required=True)

    jornada = graphene.Field('sss_backend.models.restaurant.jornadaType.JornadaType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, jor_iniciofechahora, usu_codigo, jor_finfechahora=None, jor_pedidototal=None, jor_ventatotal=None):
        try:
            jornada = Jornada.objects.create(
                jor_iniciofechahora=jor_iniciofechahora,
                jor_finfechahora=jor_finfechahora,
                jor_pedidototal=jor_pedidototal,
                jor_ventatotal=jor_ventatotal,
                usu_codigo_id=usu_codigo,
                jor_fechacreacion=datetime.now()
            )
            return CreateJornada(jornada=jornada, success=True, error=None)
        except Exception as e:
            return CreateJornada(jornada=None, success=False, error=str(e))

class UpdateJornada(graphene.Mutation):
    class Arguments:
        jor_codigo = graphene.Int(required=True)
        jor_iniciofechahora = graphene.DateTime(required=False)
        jor_finfechahora = graphene.DateTime(required=False)
        jor_pedidototal = graphene.Decimal(required=False)
        jor_ventatotal = graphene.Decimal(required=False)
        usu_codigo = graphene.Int(required=False)

    jornada = graphene.Field('sss_backend.models.restaurant.jornadaType.JornadaType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, jor_codigo, **kwargs):
        try:
            jornada = Jornada.objects.get(jor_codigo=jor_codigo)
            
            if 'jor_iniciofechahora' in kwargs:
                jornada.jor_iniciofechahora = kwargs['jor_iniciofechahora']
            if 'jor_finfechahora' in kwargs:
                jornada.jor_finfechahora = kwargs['jor_finfechahora']
            if 'jor_pedidototal' in kwargs:
                jornada.jor_pedidototal = kwargs['jor_pedidototal']
            if 'jor_ventatotal' in kwargs:
                jornada.jor_ventatotal = kwargs['jor_ventatotal']
            if 'usu_codigo' in kwargs:
                jornada.usu_codigo_id = kwargs['usu_codigo']
            
            jornada.save()
            return UpdateJornada(jornada=jornada, success=True, error=None)
        except Jornada.DoesNotExist:
            return UpdateJornada(jornada=None, success=False, error="Jornada no encontrada")
        except Exception as e:
            return UpdateJornada(jornada=None, success=False, error=str(e))

class DeleteJornada(graphene.Mutation):
    class Arguments:
        jor_codigo = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, jor_codigo):
        try:
            jornada = Jornada.objects.get(jor_codigo=jor_codigo)
            jornada.delete()
            return DeleteJornada(success=True, error=None)
        except Jornada.DoesNotExist:
            return DeleteJornada(success=False, error="Jornada no encontrada")
        except Exception as e:
            return DeleteJornada(success=False, error=str(e))

class Mutation(graphene.ObjectType):
    create_jornada = CreateJornada.Field()
    update_jornada = UpdateJornada.Field()
    delete_jornada = DeleteJornada.Field()
