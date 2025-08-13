import graphene
from graphene_django import DjangoObjectType
from sss_backend.models.restaurant import Pedido
from datetime import datetime

class CreatePedido(graphene.Mutation):
    class Arguments:
        ped_mesa = graphene.String(required=False)
        ped_tipo = graphene.String(required=False)
        ped_horarecibido = graphene.Time(required=False)
        ped_horaentrega = graphene.Time(required=False)
        ped_subtotal = graphene.Decimal(required=False)
        ped_propina = graphene.Decimal(required=False)
        ped_total = graphene.Decimal(required=False)
        ped_adicional = graphene.String(required=False)
        ped_metodopago = graphene.String(required=False)
        usu_codigo = graphene.Int(required=True)
        jor_codigo = graphene.Int(required=True)

    pedido = graphene.Field('sss_backend.models.restaurant.pedidoType.PedidoType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, usu_codigo, jor_codigo, **kwargs):
        try:
            pedido = Pedido.objects.create(
                ped_mesa=kwargs.get('ped_mesa'),
                ped_tipo=kwargs.get('ped_tipo'),
                ped_horarecibido=kwargs.get('ped_horarecibido'),
                ped_horaentrega=kwargs.get('ped_horaentrega'),
                ped_subtotal=kwargs.get('ped_subtotal'),
                ped_propina=kwargs.get('ped_propina'),
                ped_total=kwargs.get('ped_total'),
                ped_adicional=kwargs.get('ped_adicional'),
                ped_metodopago=kwargs.get('ped_metodopago'),
                usu_codigo_id=usu_codigo,
                jor_codigo_id=jor_codigo,
                ped_fechacreacion=datetime.now()
            )
            return CreatePedido(pedido=pedido, success=True, error=None)
        except Exception as e:
            return CreatePedido(pedido=None, success=False, error=str(e))

class UpdatePedido(graphene.Mutation):
    class Arguments:
        ped_codigo = graphene.Int(required=True)
        ped_mesa = graphene.String(required=False)
        ped_tipo = graphene.String(required=False)
        ped_horarecibido = graphene.Time(required=False)
        ped_horaentrega = graphene.Time(required=False)
        ped_subtotal = graphene.Decimal(required=False)
        ped_propina = graphene.Decimal(required=False)
        ped_total = graphene.Decimal(required=False)
        ped_adicional = graphene.String(required=False)
        ped_metodopago = graphene.String(required=False)
        usu_codigo = graphene.Int(required=False)
        jor_codigo = graphene.Int(required=False)

    pedido = graphene.Field('sss_backend.models.restaurant.pedidoType.PedidoType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, ped_codigo, **kwargs):
        try:
            pedido = Pedido.objects.get(ped_codigo=ped_codigo)
            
            for field, value in kwargs.items():
                if value is not None and hasattr(pedido, field):
                    if field in ['usu_codigo', 'jor_codigo']:
                        setattr(pedido, f"{field}_id", value)
                    else:
                        setattr(pedido, field, value)
            
            pedido.save()
            return UpdatePedido(pedido=pedido, success=True, error=None)
        except Pedido.DoesNotExist:
            return UpdatePedido(pedido=None, success=False, error="Pedido no encontrado")
        except Exception as e:
            return UpdatePedido(pedido=None, success=False, error=str(e))

class DeletePedido(graphene.Mutation):
    class Arguments:
        ped_codigo = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, ped_codigo):
        try:
            pedido = Pedido.objects.get(ped_codigo=ped_codigo)
            pedido.delete()
            return DeletePedido(success=True, error=None)
        except Pedido.DoesNotExist:
            return DeletePedido(success=False, error="Pedido no encontrado")
        except Exception as e:
            return DeletePedido(success=False, error=str(e))

class Mutation(graphene.ObjectType):
    create_pedido = CreatePedido.Field()
    update_pedido = UpdatePedido.Field()
    delete_pedido = DeletePedido.Field()
