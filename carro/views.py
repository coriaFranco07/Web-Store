from django.shortcuts import render
from .carro import Carro
from tienda.models import Producto
from django.shortcuts import redirect

# Create your views here.

from django.shortcuts import render
from .carro import Carro
from tienda.models import Producto
from django.shortcuts import redirect

# Create your views here.

def agregar_producto(request, producto_id):
    # Crea una instancia de la clase 'Carro' pasando el objeto 'request'.
    carro = Carro(request)
    # Obtiene el objeto 'Producto' correspondiente al 'producto_id'.
    producto = Producto.objects.get(id=producto_id)
    # Llama al método 'agregar' del carrito y pasa el producto a agregar.
    carro.agregar(producto=producto)
    # Redirige a la vista con nombre "tienda".
    return redirect("Tienda")

# Vista para eliminar un producto del carrito.
def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("Tienda")

# Vista para restar la cantidad de un producto en el carrito.
def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("Tienda")

# Vista para limpiar completamente el carrito.
def limpiar_carro(request, producto_id):
    carro = Carro(request)
    # Llama al método 'limpiar_carro' para eliminar todos los productos.
    carro.limpiar_carro()
    return redirect("Tienda")