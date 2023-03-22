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
    if request.user.is_authenticated:
        try:
            opcao_seleccionada = questao.opcao_set.get(pk=request.POST['opcao'])
        except (KeyError, Opcao.DoesNotExist):
            # Apresenta de novo o form para votar
            return render(request, 'votacao/detalhe.html',
                          {'questao': questao, 'error_message': "Não escolheu uma opção", })
        else:
            if not request.user.is_superuser:
                aluno = Aluno.objects.get(user_id=request.user.id)
                if aluno.votos == 18:
                    return render(request, 'votacao/detalhe.html',
                              {'questao': questao, 'error_message': "Limite de votos atingido", })
                aluno.votos += 1
                aluno.save()
            opcao_seleccionada.votos += 1
            opcao_seleccionada.save()

            # Retorne sempre HttpResponseRedirect depois de
            # tratar os dados POST de um form
            # pois isso impede os dados de serem tratados
            # repetidamente se o utilizador
            # voltar para a página web anterior.
            return HttpResponseRedirect(reverse('votacao:resultados', args=(questao.id,)))
    else:
        return render(request, 'votacao/detalhe.html',
                      {'questao': questao, 'error_message': "Necessita de login", })


def criarquestao(request):
    if request.method == 'POST':
        try:
            questao_texto = request.POST.get("novaquestao")
        except KeyError:
            return render(request, 'votacao/criarquestao.html')
        if questao_texto:
            questao = Questao(questao_texto=questao_texto, pub_data=timezone.now())
            questao.save()
            return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao.id,)))
        else:
            return render(request, 'votacao/criarquestao.html')
    else:
        return render(request, 'votacao/criarquestao.html')


def remover_questao(request, questao_id):
    get_object_or_404(Questao, pk=questao_id).delete()
    return HttpResponseRedirect(reverse('votacao:index'))


def criaropcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    if request.method == 'POST':
        try:
            if questao:
                questao.opcao_set.create(opcao_texto=request.POST['novaopcao'], votos=0)
                return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao.id,)))
        except KeyError:
            return render(request, 'votacao/criaropcao.html', {'questao': questao})
        else:
            return render(request, 'votacao/criaropcao.html', {'questao': questao})
    else:
        return render(request, 'votacao/criaropcao.html', {'questao': questao})


def remover_opcao(request, opcao_id, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    opcao = get_object_or_404(Opcao, pk=opcao_id).delete()
    return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao.id,)))


def registar(request):
    if request.method == 'POST':
        try:
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            Aluno.objects.create(user=user, curso=request.POST['curso'])
        except KeyError:
            return render(request, 'votacao/registar.html', {'error_message': 'Erro de login'})
        if Aluno:
            return HttpResponseRedirect(reverse('votacao:index'))
        else:
            return render(request, 'votacao/registar.html', {'error_message': 'Erro de login'})
    else:
        return render(request, 'votacao/registar.html')


def loginview(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
        except KeyError:
            return render(request, 'votacao/loginform.html', {'error_message': 'Erro de login'})
        if user:
            return HttpResponseRedirect(reverse('votacao:index'))
        else:
            return render(request, 'votacao/loginform.html', {'error_message': 'Erro de login'})
    else:
        return render(request, 'votacao/loginform.html')


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('votacao:index'))


def info_pessoal(request):
    username = request.user.username
    email = request.user.email
    data = request.user.date_joined
    u = Aluno.objects.get(user_id=request.user.id)
    curso = u.curso
    votos = u.votos
    return render(request, 'votacao/info_pessoal.html', {'username': username, 'email': email,
                                                         'data': data, 'curso': curso, 'votos': votos})
