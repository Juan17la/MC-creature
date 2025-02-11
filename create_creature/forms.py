from django import forms


class NameFormCreature(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre")
