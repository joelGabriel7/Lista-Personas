from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona, Domicilio


# Create your views here.
def bienvenido(request):
    numero = Persona.objects.count()
    name = Persona.objects.all().order_by('id')

    domi = Domicilio.objects.all()
    data = {
        'orden': numero,
        'Personas': name,
        'domicilio': domi
    }
    return render(request, 'bienvenido.html', data)


def despedirse(request):
    return HttpResponse('Despedida desde Django, Adíos!!')


def contacto(request):
    return HttpResponse('Numero: 809-703-5011, Email: Joel003@gmail.com')
