from django.shortcuts import render, redirect
from django.http import HttpResponse
from typing import Any
import json
from .models import Sala

def welcome(request) -> HttpResponse:
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
            return redirect('room_list')
        except (json.JSONDecodeError, TypeError):
            # Handle error, maybe render the form again with an error message
            return render(request, 'webapp/add_room.html', {'error': 'Invalid JSON format for available hours.'})
    return render(request, 'webapp/add_room.html')
