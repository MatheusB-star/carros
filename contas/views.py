from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from contas import forms
from django.contrib import messages
from contas import models as md
from django.urls import reverse
from django.views import View 
from django.http import HttpResponseRedirect

# Create your views here.


def novo_usuario(request):
   if request.method == 'POST':
      usuario_form = forms.usuario_form(request.POST)

      if usuario_form.is_valid():
         usuario_form.save()
         return redirect('carros_lista')
   else:
      usuario_form = forms.usuario_form()

   return render(request, 'novoUsuario.html', {'usuario_form': usuario_form})



def usuario_views(request):
    user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})




class loginview(View):

   def get(self, request):
      usuario_form = forms.usuario_form()
      return render(request, 'login.html', {'usuario_form':usuario_form})


   def post(self, request):
      usuario_form = forms.usuario_form(request.POST)
      tudocerto = True
      cpf = request.POST.get('usuario_cpf')
      senha = request.POST.get('usuario_senha')

      if not cpf:
         tudocerto = False
         messages.error(request, 'O usuário deve ser informado')
      else:
         try:
            usuario = md.usuario.objects.get(usuario_cpf=cpf)
         except md.usuario.DoesNotExist:
            tudocerto = False
            messages.error(request, 'Usuário não cadastrado no sistema')


      if not senha:
         tudocerto = False
         messages.error(request, 'A senha deve ser informada')
      else:
         try:
            autenticado = authenticate(request, username=cpf, password=senha)
            if autenticado:
               tudocerto = True
            else:
               tudocerto = False
               messages.error(request, 'Senha incorreta')

         except:
            messages.error(request, 'Não foi possível validar a senha do usuário')
            
            

      if tudocerto:
       
            usuario = md.usuario.objects.get(usuario_cpf=cpf)
            login(request, autenticado)
            nome = usuario.usuario_nome
            url = reverse('carros_lista') + f'?cpf={cpf}&nome={nome}'
            
            return HttpResponseRedirect(url)
            
      else:
         return render(request, 'login.html', {'usuario_form':usuario_form})

            
     
         



def login_view(request):
   usuario_form = forms.usuario_form(request.POST or None)
   tudocerto = True

   if request.method == 'POST':
      cpf = request.POST.get('usuario_cpf')
      senha = request.POST.get('usuario_senha')

      if not cpf:
         tudocerto = False
         messages.error(request, 'O usuário deve ser informado')
      
      if not senha:
         tudocerto = False
         messages.error(request, 'A senha deve ser informada')

      if tudocerto:
         try:
            usuario = md.usuario.objects.get(usuario_cpf=cpf)
            autenticado = authenticate(request, username=cpf, password=senha)

            if autenticado:
               login(request, autenticado)

               
               url = reverse('carros_lista') + f'?nome={usuario.usuario_nome}'

               return redirect(url)
            else:
               messages.error(request, 'Senha incorreta')
            
         except usuario.DoesNotExist:
            messages.error(request,'Usuário não cadastrado no sistema')

   return render(request, 'login.html', {'usuario_form':usuario_form})


      
def logout_view(request):
   logout(request)

   return redirect('carros_lista')


# def login_view(request):
#    tudocerto = True
#    usuario_form = forms.usuario_form(request.POST or None)
#    if request.method == 'POST':
#       cpf = request.POST.get('usuario_cpf')
#       senha = request.POST.get('usuario_senha')

#       if not cpf:
#          tudocerto = False
#          messages.error(request,'Por favor informe o usuário')
      

#       if not senha:
#          tudocerto = False
#          messages.error(request, 'Por favor informe a senha')


#       if tudocerto == True:
#          try:
#             usuario = md.usuario.objects.get(usuario_cpf=cpf)

#             if senha == usuario.usuario_senha:
#                request.session['usuario_cpf'] = usuario.usuario_cpf
#                messages.success(request, 'login realizado com sucesso')
#                return redirect('carros_lista')
            
#             else:
#                   messages.error(request, 'senha incorreta')

#          except usuario.DoesNotExist:
#             messages.error(request, 'usuário não encontrado')
#    else:
#       usuario_form = forms.usuario_form()

#    return render(request, 'login.html', {'usuario_form':usuario_form})

