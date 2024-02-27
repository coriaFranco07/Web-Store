
class Carro:
   # Constructor de la clase 'Carro'.
    def __init__(self, request):
        # Almacena el objeto 'request' recibido.
        self.request = request
        # Almacena la sesión asociada a la petición.
        self.session = request.session
        # Obtiene el contenido del carrito de la sesión.
        carro = self.session.get("carro")
        # Si no hay carrito en la sesión, crea uno vacío.
        if not carro:
            carro = self.session["carro"] = {}
        #else:
        self.carro = carro

    # Método para agregar un producto al carrito.
    def agregar(self, producto):
        # Verifica si el producto ya existe en el carrito.
        if str(producto.id) not in self.carro.keys():
            # Agrega el producto al carrito con sus detalles.
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        else:
            # Si el producto ya existe, incrementa su cantidad.
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"]= float(value["precio"])+producto.precio
                    break
        # Guarda los cambios en el carrito en la sesión.
        self.guardar_carro()

    # Método para guardar el carrito en la sesión.
    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    # Método para eliminar un producto del carrito.
    def eliminar(self, producto):
        producto.id = str(producto.id)
        # Verifica si el producto existe en el carrito y lo elimina.
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    # Método para restar la cantidad de un producto en el carrito.
    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] = value["cantidad"] - 1
                value["precio"]= float(value["precio"])-producto.precio
                # Si la cantidad llega a cero, elimina el producto.
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break
        # Guarda los cambios en el carrito en la sesión.
        self.guardar_carro()

    # Método para limpiar completamente el carrito.
    def limpiar_carro(self):
        # Vacía el contenido del carrito en la sesión.
        self.session["carro"] = {}
        self.session.modified = True