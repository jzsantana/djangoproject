# forms.py
from django import forms
from .models import Customer

class MeuModeloForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Definindo o widget para o campo 'data_nascimento' como DateInput
        self.fields['date_birth'].widget = forms.DateInput(format='%d/%m/%y', attrs={'type': 'date'})
