from django.shortcuts import redirect, render
from .forms import formularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    if request.method == "POST":
        formulario_contacto = formularioContacto(data=request.POST)
        if formulario_contacto.is_valid(): # Verificamos si los datos son validos
            
            nombre= request.POST.get("nombre") # Almacenamos la info
            email= request.POST.get("email") # Almacenamos la info
            contenido= request.POST.get("contenido") # Almacenamos la info

            email= EmailMessage("Mensaje desde Django",
            "El usuario con nombre: {}, con la direccion {}, te escribe lo siguiente: \n\n {}".format(nombre,email,contenido), 
            "",["coria9404@gmail.com"],reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?valido") # Redireccionamos de nuevo a la pagina contactos si es valido, pero con el parametro de los datos enviados
            except:
                return redirect("/contacto/?novalido")
    else:
        formulario_contacto = formularioContacto()  # Crear formulario vacío para GET


        return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})
    





