from django import forms
from .models import Articulo, Cliente, Compra

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields ='__all__'
        labels = {
            'nombre': 'Nombre',
            'email': 'Email',
            'telefono': 'Telefono',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'})
        }
        
        
class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'stock': 'Stock',
            'category': 'Categoria',
            'picture': 'Imagen'
            
        }
        widgets =  {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields ='__all__'
        labels = {
            'cliente': 'Cliente',
            'articulo': 'Articulo',
            'cantidad': 'Cantidad',
        }
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'articulo': forms.Select(attrs={'class': 'form-control'}),
	        'cantidad': forms.NumberInput(attrs={'class':'form-control'})	
        }