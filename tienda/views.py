from django.shortcuts import render
from .models import CategoriaProd, Producto

# Create your views here.

""" def producto(request):
    products = Producto.objects.all()
    return render(request, "tienda/tienda.html", {"products":products})

def categoriaProd(request, categoria_id):
    categoriaProd = CategoriaProd.objects.get(id = categoria_id)
    products = Producto.objects.filter(categorias = categoriaProd) # Filtramos los posts por las categorias
    return render(request, "tienda/categoriaProd.html", {"categoriaProd":categoriaProd, "products":products}) """

def producto(request):
    productos=Producto.objects.all()
    return render(request, "tienda/tienda.html", {"productos":productos})


