from django.shortcuts import render, HttpResponse
from carro.carro import Carro


# Create your views here.

def home(request):
    carro= Carro(request)
    return render(request, "ProyectoWebApp/home.html")


class Error403(Exception):
    def __init__(self, message="Error 403 - Prohibido"):
        self.message = message
        super().__init__(self.message)



