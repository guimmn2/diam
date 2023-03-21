from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from six import string_types
from .models import Questao, Opcao


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


def criar_questao(request):
    return render(request, 'votacao/criarquestao.html')


def guardar_questao(request):
    questao = Questao(questao_texto=request.POST['novaquestao'], pub_data=timezone.now())
    questao.save()
    return HttpResponseRedirect(reverse('votacao:index'))


def criar_opcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/criaropcao.html', {'questao': questao})


def guardar_opcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    questao.opcao_set.create(opcao_texto=request.POST['novaopcao'], votos=0)
    return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao.id,)))


def registar(request):
    return render(request, 'votacao/registar.html')


def guardar_registo(request):
    user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
    return HttpResponseRedirect(reverse('votacao:index'))


def autenticacao(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('votacao:index'))
    else:
        return render(request, 'votacao/loginform.html', {'errormessage': 'Erro de login'})
