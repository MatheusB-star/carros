from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class UsuarioManager(BaseUserManager):
    def create_user(self, usuario_cpf, usuario_email, usuario_nome, password=None, **extra_fields):
        if not usuario_cpf:
            raise ValueError('O CPF deve ser informado')
        usuario = self.model(usuario_cpf=usuario_cpf, usuario_email=usuario_email, usuario_nome=usuario_nome, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, usuario_cpf, usuario_email, usuario_nome, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(usuario_cpf, usuario_email, usuario_nome, password, **extra_fields)

class usuario(AbstractBaseUser, PermissionsMixin):
    usuario_id = models.AutoField(primary_key=True)
    usuario_cpf = models.CharField(max_length=14, unique=True)
    usuario_nome = models.CharField(max_length=60)
    usuario_email = models.EmailField(max_length=60, unique=True)
    password = models.CharField(max_length=128)  # Deve ser 'password'
    usuario_quando = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'usuario_cpf'
    REQUIRED_FIELDS = ['usuario_email', 'usuario_nome']

    def __str__(self):
        return self.usuario_nome
    

