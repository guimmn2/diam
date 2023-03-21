from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from six import string_types
from .models import Questao, Opcao, Aluno


def index(request):
    latest_question_list = Questao.objects.order_by('-pub_data')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'votacao/index.html', context)


def detalhe(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/detalhe.html', {'questao': questao})


def resultados(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/resultados.html', {'questao': questao})


def voto(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        opcao_seleccionada = questao.opcao_set.get(pk=request.POST['opcao'])
    except (KeyError, Opcao.DoesNotExist):
        # Apresenta de novo o form para votar
        return render(request, 'votacao/detalhe.html',
                      {'questao': questao, 'error_message': "Não escolheu uma opção", })
    else:
        opcao_seleccionada.votos += 1
        opcao_seleccionada.save()
        # Retorne sempre HttpResponseRedirect depois de
        # tratar os dados POST de um form
        # pois isso impede os dados de serem tratados
        # repetidamente se o utilizador
        # voltar para a página web anterior.
        return HttpResponseRedirect(reverse('votacao:resultados', args=(questao.id,)))


def criarquestao(request):
    return render(request, 'votacao/criarquestao.html')


def guardarquestao(request):
    questao = Questao(questao_texto=request.POST['novaquestao'], pub_data=timezone.now())
    questao.save()
    return HttpResponseRedirect(reverse('votacao:index'))


def criaropcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/criaropcao.html', {'questao': questao})


def guardaropcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    questao.opcao_set.create(opcao_texto=request.POST['novaopcao'], votos=0)
    return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao.id,)))


def registar(request):
    return render(request, 'votacao/registar.html')


def guardar_registo(request):
    user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
    Aluno.objects.create(user=user, curso=request.POST['curso'])
    return HttpResponseRedirect(reverse('votacao:index'))


def loginview(request):
    return render(request, 'votacao/loginform.html')


def autenticacao(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('votacao:index'))
    else:
        return render(request, 'votacao/loginform.html', {'error_message': 'Erro de login'})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('votacao:index'))


def info_pessoal(request):
    username = request.user.username
    email = request.user.email
    data = request.user.date_joined
    u = Aluno.objects.get(user_id=request.user.id)
    curso = u.curso
    return render(request, 'votacao/info_pessoal.html', {'username': username, 'email': email,
                                                         'data': data, 'curso': curso})
