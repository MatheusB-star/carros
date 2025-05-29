from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import carro

@receiver(pre_save, sender=carro)
def carro_pre_save(sender, instance, **kwargs):
    print('save')


@receiver(pre_delete, sender=carro)
def carro_pre_delete(sender, instance, **kwargs):
    print('post')


@receiver(post_delete, sender=carro)
def carro_post_delete(sender, instance, **kwargs):
    print('post_delete')


@receiver(post_save, sender=carro)
def post_save(sender, instance, **kwargs):
    print('post_save')