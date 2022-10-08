from django import forms
from .models import Docente

class DateInput(forms.DateInput):
    input_type='date'

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields ='__all__'
        widgets = {'fecha_nacimiento': DateInput(), }