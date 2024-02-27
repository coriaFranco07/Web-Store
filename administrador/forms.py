from django import forms
from blog.models import Post, Categoria
from pedidos.models import User
from servicios.models import Servicio
from tienda.models import Producto, CategoriaProd


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email'] 
        
class UserAddForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']    


class BlogEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'imagen', 'categorias', 'autor']

class BlogAddForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'imagen', 'categorias', 'autor']


class BlogCategoriaAddForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class BlogCategoriaEditForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']


class ServicioAddForm(forms.ModelForm):
   class Meta:
        model = Servicio
        fields = ['titulo', 'contenido', 'imagen']

class ServicioEditForm(forms.ModelForm):
    class Meta:
            model = Servicio
            fields = ['titulo', 'contenido', 'imagen']


class ProductoAddForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'imagen', 'precio', 'disponibilidad']

class ProductoEditForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'imagen', 'precio', 'disponibilidad']


class ProductoCategoriaAddForm(forms.ModelForm):
    class Meta:
        model = CategoriaProd
        fields = ['nombre']

class ProductoCategoriaEditForm(forms.ModelForm):
    class Meta:
        model = CategoriaProd
        fields = ['nombre']