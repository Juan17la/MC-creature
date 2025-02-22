from django.forms import ModelForm
from .models import Creature

class createCreature(ModelForm):
    class Meta:
        model = Creature
        fields = ['name']
