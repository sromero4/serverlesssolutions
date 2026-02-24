from django.shortcuts import get_object_or_404
from django.views.generic import *
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect

def panel_principal(request):
    """
    Dashboard específico para el proyecto Restaurant
    """
    return render(request, 'panel.html', {
        'project_name': 'Mapas',
        'project_icon': 'fas fa-utensils'
    })