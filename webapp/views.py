from django.shortcuts import render
from django.http import HttpResponse
from typing import Any


def welcome(request) -> HttpResponse:
    """View de boas-vindas para a aplicação de gestão de salas."""
    return render(request, 'webapp/welcome.html')
