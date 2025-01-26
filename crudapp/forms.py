from django.forms import fields
from .models import CrudappModel
from django import forms
from django.contrib.auth import models
class CrudappForm(forms.Form):
    crudapps = forms.CharField(max_length=100)
class UpdateForm(forms.ModelForm):
    class Meta:
        model = CrudappModel
        fields = ['crudapps']
        widgets = {
            'crudapps':forms.TextInput(attrs={
                'class':'form__field'
            })
        }