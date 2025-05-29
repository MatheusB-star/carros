from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import carro, car_inventory
from django.db.models import Sum

@receiver(pre_save, sender=carro)
def carro_pre_save(sender, instance, **kwargs):
    print('save')


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
