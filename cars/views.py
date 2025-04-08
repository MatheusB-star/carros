from django.shortcuts import render, redirect, get_object_or_404
from cars.models import carro
from cars import forms
from django.views import View
from django.views.generic import ListView, CreateView, DetailView






class carrosview(View):
   
   def get(self, request, cpf='0', nome='0'):
      
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
   

   
class novocarro(View):

   def get(self, request):
      novo_carroForm = forms.carromodelform()
      return render(request, 'novocarro.html', {'novo_carroForm':novo_carroForm})
   

   def post(self, request):
      novo_carroForm = forms.carromodelform(request.POST, request.FILES)

      # validando dados antes o salvamento
      if novo_carroForm.is_valid():
         novo_carroForm.save()
         return redirect('carros_lista')
      
      return render(request, 'novocarro.html', {'novo_carroForm':novo_carroForm})
   


class novo_carro(CreateView):
   model = carro
   form_class = forms.carromodelform()
   template_name = 'novocarro.html'
   success_url = '/carros_lista/'




def carros_detail(request, carro_id):
   produto = carro.objects.get(id=carro_id)
   
   produto = get_object_or_404(carro, id=carro_id)

   return render(request, 'detail.html', {'carro':produto})

# class carros_detail(DetailView):
#    model = carro
#    template_name = 'detail.html'


