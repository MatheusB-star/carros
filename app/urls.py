"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from cars import views
from contas import views as c_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', views.carrosview.as_view(), name='carros_lista'),
    path('novocarro/', views.novocarro.as_view(), name='novo_carro'),
    path('novousuario', c_views.novo_usuario, name='novo_usuario'),
    path('login_usuario', c_views.loginview.as_view(), name ='login_usuario'),
    path('logout', c_views.logout_view, name ='logout'),
    path('detalhes/<int:carro_id>', views.carros_detail, name='detalhes'),
    path('update_carro/<int:carro_id>', views.update_carro.as_view(), name='atualizar_carro'),
    path('confirmar/<int:carro_id>', views.confirmar, name='confirmar'),
    path('deletar/<int:carro_id>', views.deletar, name='deletar'),
    
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
