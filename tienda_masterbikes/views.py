from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Bicicleta
from .forms import ArriendoForm

def inicio(request):
    return render(request, 'tienda_masterbikes/inicio.html')


def catalogo(request):
    bicicletas = Bicicleta.objects.all()
    return render(request, 'tienda_masterbikes/catalogo.html', {'bicicletas': bicicletas})


@login_required
def agendar_arriendo(request):
    if request.method == 'POST':
        form = ArriendoForm(request.POST)
        if form.is_valid():
            arriendo = form.save(commit=False)
            arriendo.usuario = request.user
            arriendo.save()
            return redirect('catalogo')  # redirige después de agendar
    else:
        form = ArriendoForm()
    return render(request, 'arriendos/agendar.html', {'form': form})

