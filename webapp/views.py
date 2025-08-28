from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from typing import Any
import json
from .models import Sala

def welcome(request: HttpRequest) -> HttpResponse:
    """View de boas-vindas para a aplicação de gestão de salas."""
    return render(request, 'webapp/welcome.html')

def room_list(request):
    """
    View to list all rooms.
    """
    rooms = Sala.objects.all()
    return render(request, 'webapp/room_list.html', {'rooms': rooms})

def add_room(request):
    """
    View to add a new room.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        available_hours_str = request.POST.get('available_hours')
        try:
            available_hours = json.loads(available_hours_str)
            Sala.objects.create(name=name, available_hours=available_hours)
            return redirect('webapp:room_list')
        except (json.JSONDecodeError, TypeError):
            # Handle error, maybe render the form again with an error message
            return render(request, 'webapp/add_room.html', {'error': 'Invalid JSON format for available hours.'})
    return render(request, 'webapp/add_room.html')

def user_login(request: HttpRequest) -> HttpResponse:
    """View para autenticação de usuário."""
    if request.user.is_authenticated:
        return redirect('webapp:welcome')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo, {username}!')
                return redirect('webapp:welcome')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')
    
    return render(request, 'webapp/login.html')


def user_logout(request: HttpRequest) -> HttpResponse:
    """View para logout do usuário."""
    logout(request)
    messages.success(request, 'Você foi desconectado com sucesso.')
    return redirect('webapp:login')


def user_register(request: HttpRequest) -> HttpResponse:
    """View para cadastro de novo usuário."""
    if request.user.is_authenticated:
        return redirect('webapp:welcome')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('webapp:welcome')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = UserCreationForm()
    
    return render(request, 'webapp/register.html', {'form': form})


@login_required
def dashboard(request: HttpRequest) -> HttpResponse:
    """View do dashboard (apenas para usuários autenticados)."""
    return render(request, 'webapp/dashboard.html')
