from audioop import reverse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from pedidos.models import LineaPedido, Pedido
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
# Create your views here.

@login_required(login_url="/autenticacion/loguear")  # Requiere que el usuario esté autenticado para acceder a la vista
def procesar_pedido(request):

    pedido = Pedido.objects.create(user=request.user)  # Crea un nuevo pedido asociado al usuario actual
    carro = Carro(request)  # Crea una instancia del carrito de compras basada en la solicitud
    lineas_pedido = list()  # Crea una lista para almacenar las líneas de pedido

    for key, value in carro.carro.items():  # Itera a través de los elementos en el carrito
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        ))  # Crea una línea de pedido y la agrega a la lista

    LineaPedido.objects.bulk_create(lineas_pedido)  # Inserta las líneas de pedido en la base de datos
    
    # Calcula subtotales y total del pedido
    total_pedido = 0
    for linea_pedido in lineas_pedido:
        linea_pedido.subtotal = linea_pedido.cantidad * linea_pedido.producto.precio
        total_pedido += linea_pedido.subtotal

    enviar_mail(
    pedido=pedido,
    lineas_pedido=lineas_pedido,
    nombre_usuario=request.user.username,
    email_usuario=request.user.email,
    total_pedido=total_pedido,
    ) 

    messages.success(request, "El pedido se ha creado correctamente")  # Muestra un mensaje de éxito al usuario
    return redirect("../tienda")

   


def enviar_mail(**kawargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido.html",{
    "pedido": kawargs.get("pedido"),
    "lineas_pedido": kawargs.get("lineas_pedido"),
    "nombre_usuario": kawargs.get("nombre_usuario")
    })

    mensaje_texto=strip_tags(mensaje)
    from_email="coria9404@gmail.com"
    to=kawargs.get("email_usuario")
    #to="francoria1921@gmail.com"
    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)


""" enviar_mail(
    pedido=pedido,
    lineas_pedido=lineas_pedido,
    nombre_usuario=request.user.username,
    email_usuario=request.user.email,
    total_pedido=total_pedido,
    )  """
