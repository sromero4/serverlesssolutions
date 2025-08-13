import graphene
from graphene_django import DjangoObjectType
from sss_backend.models.restaurant import Producto
from datetime import datetime

class CreateProducto(graphene.Mutation):
    class Arguments:
        prod_nombre = graphene.String(required=True)
        prod_precio = graphene.Decimal(required=True)
        prod_descripcion = graphene.String(required=False)
        prod_imagen = graphene.String(required=False)
        est_codigo = graphene.Int(required=True)
        usu_codigo = graphene.Int(required=True)

    producto = graphene.Field('sss_backend.models.restaurant.productoType.ProductoType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, prod_nombre, prod_precio, est_codigo, usu_codigo, prod_descripcion=None, prod_imagen=None):
        try:
            producto = Producto.objects.create(
                prod_nombre=prod_nombre,
                prod_precio=prod_precio,
                prod_descripcion=prod_descripcion,
                prod_imagen=prod_imagen,
                est_codigo_id=est_codigo,
                usu_codigo_id=usu_codigo,
                prod_fechacreacion=datetime.now()
            )
            return CreateProducto(producto=producto, success=True, error=None)
        except Exception as e:
            return CreateProducto(producto=None, success=False, error=str(e))

class UpdateProducto(graphene.Mutation):
    class Arguments:
        prod_codigo = graphene.Int(required=True)
        prod_nombre = graphene.String(required=False)
        prod_descripcion = graphene.String(required=False)
        prod_precio = graphene.Decimal(required=False)
        prod_imagen = graphene.String(required=False)
        est_codigo = graphene.Int(required=False)
        usu_codigo = graphene.Int(required=False)

    producto = graphene.Field('sss_backend.models.restaurant.productoType.ProductoType')
    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, prod_codigo, **kwargs):
        try:
            producto = Producto.objects.get(prod_codigo=prod_codigo)
            
            if 'prod_nombre' in kwargs:
                producto.prod_nombre = kwargs['prod_nombre']
            if 'prod_descripcion' in kwargs:
                producto.prod_descripcion = kwargs['prod_descripcion']
            if 'prod_precio' in kwargs:
                producto.prod_precio = kwargs['prod_precio']
            if 'prod_imagen' in kwargs:
                producto.prod_imagen = kwargs['prod_imagen']
            if 'est_codigo' in kwargs:
                producto.est_codigo_id = kwargs['est_codigo']
            if 'usu_codigo' in kwargs:
                producto.usu_codigo_id = kwargs['usu_codigo']
            
            producto.prod_fechamodificacion = datetime.now()
            producto.save()
            return UpdateProducto(producto=producto, success=True, error=None)
        except Producto.DoesNotExist:
            return UpdateProducto(producto=None, success=False, error="Producto no encontrado")
        except Exception as e:
            return UpdateProducto(producto=None, success=False, error=str(e))

class DeleteProducto(graphene.Mutation):
    class Arguments:
        prod_codigo = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, prod_codigo):
        try:
            producto = Producto.objects.get(prod_codigo=prod_codigo)
            producto.delete()
            return DeleteProducto(success=True, error=None)
        except Producto.DoesNotExist:
            return DeleteProducto(success=False, error="Producto no encontrado")
        except Exception as e:
            return DeleteProducto(success=False, error=str(e))

class Mutation(graphene.ObjectType):
    create_producto = CreateProducto.Field()
    update_producto = UpdateProducto.Field()
    delete_producto = DeleteProducto.Field()
