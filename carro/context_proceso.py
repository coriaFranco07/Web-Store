
def importe_total_carro(request):
    total = 0  # Inicializa el total en cero.

    # Verifica si el usuario está autenticado.
    if request.user.is_authenticated:
        # Verifica si hay un carrito en la sesión.
        if 'carro' in request.session:
            # Itera a través de los elementos del carrito en la sesión.
            for key, value in request.session["carro"].items():
                # Calcula el subtotal del producto y lo agrega al total.
                total = total + float(value["precio"])
    else:
        total="Debes hacer Login"

    # Retorna un diccionario con la clave "importe_total_carro" y el valor total calculado.
    return {"importe_total_carro": total}