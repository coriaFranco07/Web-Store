from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.

class VRegistro(View):
    def get(self, request):
        form= CustomUserCreationForm()
        return render(request, "registro/registro.html", {'form':form})

    def post(self, request):
        form= CustomUserCreationForm(request.POST) # Almacenamos el usuario y la contraseña que ingreso el usuario
        if form.is_valid(): # Comprobamos si el formulario es valido
            usuario= form.save() # Almacenamos la info del formulario
            login(request, usuario) 
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro/registro.html", {'form':form})
        
"""     La función login() realiza las siguientes acciones: """

"""     Autenticación: Verifica las credenciales del usuario proporcionadas en el objeto user. Si las credenciales son válidas y el usuario existe en la base de datos, el usuario se considera autenticado.

        Establecer sesión: Crea una sesión para el usuario autenticado. Una sesión es un mecanismo que permite que la aplicación rastree la actividad de un usuario a medida que navega por diferentes páginas.

        Cookies: La función login() también establece una cookie en el navegador del usuario, que contiene información sobre la sesión. Esto permite que el usuario siga siendo autenticado en visitas posteriores mientras la sesión esté activa. """

def cerrar_sesion(request):
    logout(request)
    return redirect('Home')


def loguear(request):
    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            nombre_usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contraseña)
            
            if usuario is not None:

                login(request, usuario)
                return redirect("Home")
                    
            else:
                
                messages.error(request, "Usuario no válido")
        else:

            messages.error(request, "Información incorrecta")
    else:

        form = AuthenticationForm()
    
    return render(request, "login/login.html", {"form": form})