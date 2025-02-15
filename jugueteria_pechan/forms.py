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
    articulo = forms.ModelMultipleChoiceField(
        queryset=Articulo.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=True,
        label="Artículo"
    )
    
    fecha_compra = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label="Fecha de compra"
    )

    class Meta:
        model = Compra
        fields = ['cliente', 'articulo', 'fecha_compra']  
        labels = {
            'cliente': 'Cliente',
            'articulo': 'Artículo',
            'fecha_compra': 'Fecha de compra',
        }
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }