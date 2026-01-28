from django.shortcuts import get_object_or_404
from django.views.generic import *
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .forms import *
from .models import *


class CrearIngrediente(SuccessMessageMixin, CreateView):
    model = Ingrediente
    form_class = CrearIngredienteForm
    template_name = "add_ingredientes.html"
    success_url = reverse_lazy('list_ingredientes')
    success_message = "¡El ingrediente se creó con exito!"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CrearIngrediente, self).dispatch(request, *args, **kwargs)

    def form_valid(self,form):
        ingrediente = form.instance
        self.object = form.save()
        return super(CrearIngrediente, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CrearIngrediente, self).get_context_data(**kwargs)
        context['modificar'] = False
        context['menu_ingrediente'] = True
        return context


class ListarIngredientes(ListView):
    model = Ingrediente
    template_name = "list_ingredientes.html"

    def get_queryset(self):
        queryset = super(ListarIngredientes, self).get_queryset()
        return queryset.order_by('-pk')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ListarIngredientes, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ListarIngredientes, self).get_context_data(**kwargs)
        context['menu_ingrediente'] = True
        return context


class EditarIngrediente(SuccessMessageMixin, UpdateView):
    model = Ingrediente
    form_class = CrearIngredienteForm
    template_name = "list_ingredientes.html"
    success_url = reverse_lazy('listar_ingredientes')
    success_message = "¡El ingrediente fue modificada con exito!"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(EditarIngrediente, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EditarIngrediente, self).get_context_data(**kwargs)
        context['modificar'] = True
        context['menu_ingrediente'] = True
        return context


def eliminar_ingrediente(request):
    ing_codigo = request.GET.get('id', '')
    mi_ingrediente = get_object_or_404(Ingrediente, pk=ing_codigo)
    mi_ingrediente.delete()
    messages.success(request, 'Ingrediente eliminada con exito!')
    data = {
        'eliminacion': True,
    }
    return JsonResponse(data)