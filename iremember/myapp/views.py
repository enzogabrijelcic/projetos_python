from django.shortcuts import redirect, render
# Create your views here.
from .forms import UserLoginForm, UserRegistrationForm
import requests

def index(request):
    return render(request, 'index.html')
#def enzo(request):
#    return render(request, 'enzo.html')

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            # Preparar dados para enviar à API
            data = {
                'nome': form.cleaned_data['nome'],
                'senha': form.cleaned_data['senha']
            }

            # Enviar formulário para a API (exemplo)
            api_response = requests.post('https://api-python-tarde-37668b622097.herokuapp.com/login', json=data)
            # Lógica de tratamento da resposta da API#joga para view index
            api_data = api_response.json()
            if api_response.status_code == 200:
                # Se a resposta da API foi bem-sucedida (status code 200)
                # Exemplo: receber dados da API (JSON)
                
                sucess_message = api_data
                # Exemplo: passar os dados para a próxima página
                return render(request, 'ok.html', {'api_data': api_data,'sucess_message':sucess_message})

            else:
                # Se a resposta da API não foi bem-sucedida
                # Exemplo: exibir mensagem de erro para o usuário
                error_message = api_data
                return render(request, 'erro.html', {'form': form, 'error_message': error_message})

           
    else:
        form = UserLoginForm()
   
    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Preparar dados para enviar à API
            data = {
                'nome': form.cleaned_data['nome'],
                'senha': form.cleaned_data['senha'],
                'email': form.cleaned_data['email'],
                'cpf': form.cleaned_data['cpf']
            }

            # Enviar formulário para a API (exemplo)
            api_response = requests.post('https://api-python-tarde-37668b622097.herokuapp.com/register', json=data)
            # Lógica de tratamento da resposta da API#joga para view index
            api_data = api_response.json()
            if api_response.status_code == 200:
                # Se a resposta da API foi bem-sucedida (status code 200)
                # Exemplo: receber dados da API (JSON)
                
                sucess_message = api_data
                # Exemplo: passar os dados para a próxima página
                return render(request, 'ok.html', {'api_data': api_data,'sucess_message':sucess_message})

            else:
                # Se a resposta da API não foi bem-sucedida
                # Exemplo: exibir mensagem de erro para o usuário
                error_message = api_data
                return render(request, 'erro.html', {'form': form, 'error_message': error_message})

           
    else:
        form = UserRegistrationForm()
   
    return render(request, 'register.html', {'form': form})