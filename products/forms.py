from django import forms
from . import models

# Creo una clase la cual va a contener la estructura del formulario para agregar una Categoría
class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['name']

# Creo una clase la cual va a contener la estructura del formulario para agregar un Tipo
class TypeForm(forms.ModelForm):
    class Meta:
        model = models.Type
        fields = ['name']

# Creo una clase la cual va a contener la estructura del formulario para agregar un Producto
class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'price', 'category_id', 'type_id', 'image']

    # Con esta función sobrecargo la inicialización del formulario para que este tenga todas las opciones disponibles que hayan en Category
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category_id'].queryset = models.Category.objects.all()
        self.fields['type_id'].queryset = models.Type.objects.all()

    # Función para validar el campo de precio
    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("El precio debe ser mayor que 0.")
        return price