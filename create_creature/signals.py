from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Collection
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_collection(sender, instance, created, **kwargs):
    if created:
        Collection.objects.create(User=instance)
