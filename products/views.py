from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from . import models
from .forms import ProductForm, CategoryForm, TypeForm
from cart.cart import Cart
from cart import forms

# View para página principal
def index(request):
    # Obtención de productos
    products1 = models.Product.objects.all()[0:4]
    products2 = models.Product.objects.all()[4:8]

    form = forms.AddToCartForm()
    context = {
        'products1': products1,
        'products2': products2,
        'form': form
    }
    return render(request, 'products/index.html', context)

# View para página nosotros
def about(request):
    return render(request, 'products/about.html')

# View para página perro
def dog(request):
    form = forms.AddToCartForm()
    # Crear lista solo para agregar productos de tipo Perro
    dog_list = []

    for product in models.Product.objects.all():
        if product.type_id.type_id == 1:
            dog_list.append(product)

    context = {
        'products': dog_list,
        'form': form
    }
    return render(request, 'products/dog.html', context)

# View para página gato
def cat(request):
    form = forms.AddToCartForm()
    # Crear lista solo para agregar productos de tipo Gato
    cat_list = []

    for product in models.Product.objects.all():
        if product.type_id.type_id == 2:
            cat_list.append(product)

    context = {
        'products': cat_list,
        'form': form
    }
    return render(request, 'products/cat.html', context)

# View para página de carro
def cart(request):
    cart = Cart(request)

    context = {
        'cart': cart
    }
    return render(request, 'products/cart.html', context)

# View para ver el catálogo de productos
@login_required
def catalogue(request):
    products = models.Product.objects.all()
    categories = models.Category.objects.all()
    types = models.Type.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'types': types
    }
    return render(request, 'products/catalogue.html', context)

""" CREATE FUNCTIONS """

# View para agregar una nueva categoría
@login_required
def new_category(request):
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = CategoryForm()
    else:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    
    context = {
        'form': form
    }
    return render(request, 'products/new_category.html', context)

# View para agregar nuevo tipo
@login_required
def new_type(request):
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TypeForm()
    else:
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    
    context = {
        'form': form
    }
    return render(request, 'products/new_type.html', context)

# View para agregar un nuevo producto
@login_required
def new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProductForm()
    
    context = {
        'form': form
    }
    return render(request, 'products/new_product.html', context)

""" EDIT FUNCTIONS """

# View para editar una categoría
@login_required
def edit_category(request, category_id):
    # Obtengo el objeto de la categría que quiere modificar el usuario
    category = get_object_or_404(models.Category, pk=category_id)

    if request.method != 'POST':
        # Si es que la petición es diferente de POST se rellena el formulario con la información de la categoría obtenida
        form = CategoryForm(instance=category)
    else:
        # El método de la petición es POST, por lo tanto se procesa la información que se rellenó en el formulario
        form = CategoryForm(instance=category, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    
    context = {
        'form': form,
        'category': category
    }
    return render(request, 'products/edit_category.html', context)

# View para editar un tipo
@login_required
def edit_type(request, type_id):
    # Obtengo el objeto del tipo que quiere modificar el usuario
    type = get_object_or_404(models.Type, pk=type_id)

    if request.method != 'POST':
        # Si es que la petición es diferente de POST se rellena el formulario con la información del producto obtenido
        form = TypeForm(instance=type)
    else:
        # El método de la petición es POST, por lo tanto se procesa la información que se rellenó en el formulario
        form = TypeForm(instance=type, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'type': type
    }
    return render(request, 'products/edit_type.html', context)

# View para editar un producto
@login_required
def edit_product(request, product_id):
    # Obtener objeto a modificar por usuario
    product = get_object_or_404(models.Product, pk=product_id)

    if request.method != 'POST':
        # Si es que la petición es diferente de POST se rellena el formulario con la información del producto obtenido
        form = ProductForm(instance=product)
    else:
        # El método de la petición es POST, por lo tanto se procesa la información que se rellenó en el formulario
        form = ProductForm(instance=product, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'product': product
    }
    return render(request, 'products/edit_product.html', context)

""" DELETE FUNCTIONS """

# View para eliminar una categoría
@login_required
def delete_category(request, category_id):
    # Obtener categoría a eliminar por usuario
    category = get_object_or_404(models.Category, pk=category_id)

    if request.method == 'POST':
        category.delete()
        return redirect('catalogue')

    context = {
        'category': category
    }
    return render(request, 'products/delete_category.html', context)

# View para eliminar un tipo
@login_required
def delete_type(request, type_id):
    # Obtener tipo a eliminar por usuario
    type = get_object_or_404(models.Type, pk=type_id)

    if request.method == 'POST':
        type.delete()
        return redirect('catalogue')
    
    context = {
        'type': type
    }
    return render(request, 'products/delete_type.html', context)

# View para eliminar un producto
@login_required
def delete_product(request, product_id):
    # Obtener producto a eliminar por usuario
    product = get_object_or_404(models.Product, pk=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('catalogue')

    context = {
        'product': product
    }
    return render(request, 'products/delete_product.html', context)