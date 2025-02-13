from django import forms

class NameFormCreature(forms.Form):
    name = forms.CharField(
        label="Nombre de la Criatura",  # Cambia el texto del label
        widget=forms.TextInput(attrs={'class': 'input-minecraft'}),
    )
