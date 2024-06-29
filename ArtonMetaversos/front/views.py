from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Raca


def index(request):
    return render(request, 'site/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso')
            return redirect('/')
        else:
            messages.error(request, 'Username ou senha incorretos')
    return render(request, 'site/login.html')

def registrar(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username já registrado')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email já registrado')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                login(request, user)
                messages.success(request, 'Registro realizado com sucesso')
                return redirect('/')
        else:
            messages.error(request, 'Senhas não coincidem')
    return render(request, 'site/registrar.html')


@login_required
def dashboard_home(request):
    # Busca todas as raças criadas
    racas = Raca.objects.all()

    context = {
        'racas': racas
    }
    return render(request, 'dashboard/home.html', context)

@login_required
def manage_games(request):
    return render(request, 'dashboard/manage_games.html')

@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')

@login_required
def settings(request):
    return render(request, 'dashboard/settings.html')

@login_required
def criar_raca(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        atributos = ', '.join(request.POST.getlist('atributos'))
        habilidades = ', '.join(request.POST.getlist('habilidades'))
        logica_de_criacao = request.POST['logica_de_criacao']
        
        raca = Raca(
            nome=nome,
            descricao=descricao,
            atributos=atributos,
            habilidades=habilidades,
            logica_de_criacao=logica_de_criacao,
            autor=request.user,
            versao='1.0'
        )
        raca.save()
        return redirect('/dashboard')  # Redirecione para uma página apropriada após a criação
        
    return render(request, 'dashboard/raca/criar.html')

def detalhes_raca(request, raca_id):
    raca = get_object_or_404(Raca, pk=raca_id)

    context = {
        'raca': raca
    }
    return render(request, 'dashboard/raca/detalhes.html', context)

@login_required
def lista_racas(request):
    return render(request, 'dashboard/raca/lista.html')