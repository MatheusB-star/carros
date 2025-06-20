from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import carro, car_inventory
from django.db.models import Sum
import google.generativeai as genai
from .utils import gerar_bio_carro

@receiver(pre_save, sender=carro)
def carro_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = gerar_bio_carro(
            instance.modelo,
            instance.marca,
            instance.ano_fabricacao,
            instance.ano_modelo,
            instance.valor
        )



@receiver(pre_delete, sender=carro)
def carro_pre_delete(sender, instance, **kwargs):
    print('post')



@receiver([post_save, post_delete], sender=carro)
def post_save(sender, instance, **kwargs):
    car_count = carro.objects.all().count()
    car_value = carro.objects.aggregate(
        total = Sum('valor')
    )['total']

    car_inventory.objects.create(
        car_count = car_count,
        car_value = car_value
    )


# def teste():
#     print('entrou')

   
#     genai.configure(api_key="AIzaSyDtxrHX7CKfz7IhG1iSu_765YTHC7LVlLs")

#     model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

#     response = model.generate_content("explique pra mim em poucas palavras como funciona uma IA")

#     print(response.text)

# teste()

