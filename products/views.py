from django.shortcuts import render
from . import models

import random

# Función para retornar valores aleatorios de una lista
def randomProducts(products_list, total):
    products = []

    for i in range(0, total):
        aleatory = products_list[random.randint(0, len(products_list) - 1)]
        products.append(aleatory)

    return products

# View para página principal
def index(request):
    # Obtención de productos
    products1 = randomProducts(models.Product.objects.all(), 4)
    products2 = randomProducts(models.Product.objects.all(), 4)

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