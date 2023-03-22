from django import forms
from .models import Product

class MyForm(forms.Form):
    name = forms.CharField(label='Твое имя', max_length=50)
    age = forms.IntegerField(label='Возраст')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'foto' )


