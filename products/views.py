from django.shortcuts import render
from . import models

# View para página principal
def index(request):
    # Obtención de productos
    products1 = models.Product.objects.all()[0:4]
    products2 = models.Product.objects.all()[4:8]

    context = {
        'products1': products1,
        'products2': products2
    }
    return render(request, 'products/index.html', context)

# View para página nosotros
def about(request):
    return render(request, 'products/about.html')

# View para página perro
def dog(request):
    # Crear lista solo para agregar productos de tipo Perro
    dog_list = []

    for product in models.Product.objects.all():
        if product.type_id.type_id == 1:
            dog_list.append(product)

    context = {
        'products': dog_list
    }
    return render(request, 'products/dog.html', context)

# View para página gato
def cat(request):
    # Crear lista solo para agregar productos de tipo Gato
    cat_list = []

    for product in models.Product.objects.all():
        if product.type_id.type_id == 2:
            cat_list.append(product)

    context = {
        'products': cat_list
    }
    return render(request, 'products/cat.html', context)

# View para página de carro
def cart(request):
    return render(request, 'products/cart.html')