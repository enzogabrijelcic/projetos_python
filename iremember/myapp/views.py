from django.shortcuts import redirect, render

# Create your views here.
from .forms import UserLoginForm, UserRegistrationForm
import requests

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            # Enviar formulário para a API (exemplo)
            api_response = requests.post('https://api-python-tarde-37668b622097.herokuapp.com/login', data=form.cleaned_data)
            # Lógica de tratamento da resposta da API#joga para view index
            return redirect('index')
    else:
        form = UserLoginForm()
   
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Enviar formulário para a API (exemplo)
            api_response = requests.post('https://api-python-tarde-37668b622097.herokuapp.com/register', data=form.cleaned_data)
            # Lógica de tratamento da resposta da API#joga para view index
            return redirect('index')
    else:
        form = UserRegistrationForm()
   
    return render(request, 'register.html', {'form': form})