from django import forms
from .models import Product, Assembly, Component, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['customer']


class AssemblyForm(forms.ModelForm):
    class Meta:
        model = Assembly
        fields=['name']


class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        exclude=['assembly']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'



