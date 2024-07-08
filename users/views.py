from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Vista para iniciar sesión
def login_view(request):
    if request.method != 'POST':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)

# Vista para cerrar sesión
def logout_view(request):
    logout(request)
    return redirect('login')

# Vista para registrarse como usuario
def register(request):
    if request.method != 'POST':
        # Se muestra un formulario en blanco
        form = UserCreationForm()
    else:
        # En este caso el formulario debería estar rellenado
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Se registra al usuario y se envía a la página de inicio
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return redirect('index')
    
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)