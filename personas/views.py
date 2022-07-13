from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from personas.forms import PersonaForm
from personas.models import Persona


def detallePersona(request, id):
    # detalle = Persona.objects.get(pk=id)
    detalle = get_object_or_404(Persona, pk=id)
    data = {
        'detalle': detalle
    }
    return render(request, 'persona/detalle.html', data)

# PersonaForm = modelform_factory(Persona, exclude=[] )

def nuevaPersona(request):
    formaPersona = PersonaForm()
    data = {
        'formaPersona': formaPersona
    }
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('home')
    else:
        return render(request, 'persona/nuevo.html', data)



def editarPersona(request, id):
    detalle = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST,instance=detalle)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('home')
    else:

        formaPersona2= PersonaForm(instance=detalle)
        data2 = {
            'formaPersona': formaPersona2
        }
    return render(request, 'persona/editar.html', data2,)


def eliminarPersona(request, id):
    detalle = get_object_or_404(Persona, pk=id)
    if detalle:
        detalle.delete()
    return redirect('home')