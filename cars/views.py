from django.shortcuts import render, redirect, get_object_or_404
from cars.models import carro
from cars import forms
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin





class carrosview(LoginRequiredMixin, View):
   login_url = 'login_usuario'
   
   def get(self, request):
      cpf = self.request.GET.get('cpf')
      nome = self.request.GET.get('nome')
      search = request.GET.get('search')

      if search:
         carros = carro.objects.filter(modelo__icontains=search)
      else:
         carros = carro.objects.all().order_by('modelo')
         
      
      return render(request, 'carros.html', {'carros': carros,'cpf': cpf, 'nome': nome})
      



class carros_view(ListView):
   model = carro
   template_name = 'carros.html'
   context_object_name = 'carros'

   def get_queryset(self, cpf, nome):
      carros = super().get_queryset().order_by('modelo')
      search = self.request.GET.get('search')
      if search:
         carros = carros.filter(modelo__icontains=search)
      
      return carros
   


class update_carro(View):

   def get(self, request, carro_id):
      objeto = get_object_or_404(carro, id=carro_id)
      novo_carroForm = forms.carromodelform(instance=objeto)
      return render(request, 'novocarro.html', {'novo_carroForm': novo_carroForm, 'carro': objeto})
   

   def post(self, request, carro_id):
      objeto = get_object_or_404(carro, id=carro_id)
      form = forms.carromodelform(request.POST, instance=objeto)

      if form.is_valid():
         form.save()
         return redirect('detalhes', carro_id=objeto.id)
      
      return render(request, 'novocarro.html', {'novo_carroForm': form, 'carro':objeto})
      


class delete_carro(DeleteView):
   model = carro
   template_name = 'confirmar.html'


   def delete(self, request, *args, **kwargs):
    print("DELETANDO...")
    return super().delete(request, *args, **kwargs)
   
   
   def get_success_url(self):
      cpf = self.request.POST.get('cpf')
      nome = self.request.POST.get('nome')

      url = reverse('carros_lista') + f'?cpf={cpf}&nome={nome}'
      return HttpResponseRedirect(url)


# def confirmar(request, carro_id):
#    objeto = get_object_or_404(carro, id=carro_id)
#    cpf = request.GET.get('cpf')
#    nome = request.GET.get('nome')
#    return render(request,'confirmar.html', {'carro': objeto, 'cpf':cpf, 'nome': nome})



   
@require_POST
def deletar(request, carro_id):
   print('entrou')
   objeto = get_object_or_404(carro, id=carro_id)
   objeto.delete()
   cpf = request.GET.get('cpf')
   nome = request.GET.get('nome')
   url = reverse('carros_lista') + f'?cpf={cpf}&nome={nome}'
   
   response = HttpResponse()
   response["HX-Redirect"] = url
   return response

   


 
class novocarro(LoginRequiredMixin, View):
   login_url = 'login_usuario'

   def get(self, request, cpf=0, nome=0):
      novo_carroForm = forms.carromodelform()
      return render(request, 'novocarro.html', {'novo_carroForm':novo_carroForm, 'cpf': cpf, 'nome': nome})
   

   def post(self, request, cpf=0, nome=0):
      novo_carroForm = forms.carromodelform(request.POST, request.FILES)

      # validando dados antes o salvamento
      if novo_carroForm.is_valid():
         novo_carroForm.save()
         url = reverse('carros_lista') + f'?cpf={cpf}&nome={nome}'
         return HttpResponseRedirect(url)
      
      return render(request, 'novocarro.html', {'novo_carroForm':novo_carroForm, 'cpf': cpf, 'nome': nome})
   


class novo_carro(CreateView):
   model = carro
   form_class = forms.carromodelform()
   template_name = 'novocarro.html'
   success_url = '/carros_lista/'




def carros_detail(request, carro_id):
   produto = carro.objects.get(id=carro_id)
   
   produto = get_object_or_404(carro, id=carro_id)
   cpf = request.GET.get('cpf')
   nome = request.GET.get('nome')

   return render(request, 'detail.html', {'carro':produto, 'cpf': cpf, 'nome': nome})

# class carros_detail(DetailView):
#    model = carro
#    template_name = 'detail.html'


