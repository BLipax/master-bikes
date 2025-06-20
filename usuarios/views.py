from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('catalogo')  # redirige a donde tú quieras
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('catalogo')  # Redirige donde tú quieras
        else:
            error = "Usuario o contraseña incorrectos"
            return render(request, 'usuarios/login.html', {'error': error})
    return render(request, 'usuarios/login.html')
