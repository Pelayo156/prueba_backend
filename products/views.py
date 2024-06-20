from django.shortcuts import render

# View para página principal
def index(request):
    return render(request, 'products/index.html')

# View para página nosotros
def about(request):
    return render(request, 'products/about.html')

# View para página perro
def dog(request):
    return render(request, 'products/dog.html')

# View para página gato
def cat(request):
    return render(request, 'products/cat.html')

# View para página de carro
def cart(request):
    return render(request, 'products/cart.html')