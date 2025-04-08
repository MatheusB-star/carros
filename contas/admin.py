from django.contrib import admin
from contas import models as md

# Register your models here.
class usuario_admin(admin.ModelAdmin):
    list_display = ('usuario_id', 'usuario_cpf', 'usuario_nome', 'usuario_email', 'password', 'usuario_quando')
    search_fields = ('usuario_id',)








admin.site.register(md.usuario, usuario_admin)