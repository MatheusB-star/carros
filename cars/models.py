from django.db import models


class marca(models.Model):
    id = models.AutoField(primary_key=True)
    marca_nome = models.CharField(max_length=60)


    def __str__(self):
        return self.marca_nome



class carro(models.Model):
    id = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=200)
    marca = models.ForeignKey(marca, on_delete=models.PROTECT, related_name='carro_marca')
    ano_fabricacao = models.IntegerField(blank=True, null=True)
    ano_modelo = models.IntegerField(blank=True, null=True)
    placa = models.CharField(max_length=10, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    carro_foto = models.ImageField(upload_to='cars/', blank=True, null=True)
    
    
    def __str__(self):
        return self.modelo



    


    