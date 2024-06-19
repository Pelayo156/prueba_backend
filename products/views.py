from django.shortcuts import render

# View para página principal
def index(request):
    return render(request, 'products/index.html')