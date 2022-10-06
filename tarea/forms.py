from django import forms
from .models import Tarea

class DateInput(forms.DateInput):
    input_type='date'

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields ='__all__'
        widgets = {'fechaVencimiento': DateInput(),}