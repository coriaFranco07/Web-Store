from django.shortcuts import render
from .models import Post, Categoria
from django.contrib.auth.decorators import permission_required

# Create your views here.

def post(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts":posts})

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id = categoria_id)
    posts = Post.objects.filter(categorias = categoria) # Filtramos los posts por las categorias
    return render(request, "blog/categoria.html", {"categoria":categoria, "posts":posts})
