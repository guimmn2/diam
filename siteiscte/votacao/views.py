from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *  # (2)
from .models import Questao, Opcao, Aluno
@api_view(['GET', 'POST'])  # (3)
def questoes_lista(request):
    if request.method == 'GET':  # (4)
        questoes = Questao.objects.all()
        serializerQ = QuestaoSerializer(questoes, context={'request': request}, many=True)
        return Response(serializerQ.data)
    elif request.method == 'POST':  # (4)
        serializer = QuestaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])  # (3) e (5)
def questoes_edita(request, pk):
    try:
        questao = Questao.objects.get(pk=pk)
    except Questao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = QuestaoSerializer(questao, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        questao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def opcoes_lista(request):
    if request.method == 'GET':
        opcoes = Opcao.objects.all()
        serializerO = OpcaoSerializer(opcoes, context={'request': request}, many=True)
        return Response(serializerO.data)
    elif request.method == 'POST':
        serializer = OpcaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def opcoes_edita(request, pk):
    try:
        opcao = Opcao.objects.get(pk=pk)
    except Opcao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = OpcaoSerializer(opcao, data=request.data, context={'request': request})
        if serializer.is_valid():
            opcao.votos = opcao.votos + 1
            opcao.save()
            # serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        opcao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def check_superuser(user):
    return user.is_superuser


def index(request):
    latest_question_list = Questao.objects.order_by('-pub_data')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'votacao/index.html', context)


def detalhe(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/detalhe.html', {'questao': questao})


@login_required(login_url=reverse_lazy('votacao:login'))
def voto(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        opcao_seleccionada = questao.opcao_set.get(pk=request.POST['opcao'])
    except (KeyError, Opcao.DoesNotExist):
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
        return render(request, 'votacao/resultados.html', {'questao': questao})


@user_passes_test(check_superuser, login_url=reverse_lazy('votacao:detalhe'))
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


@user_passes_test(check_superuser, login_url=reverse_lazy('votacao:detalhe'))
def remover_questao(request, questao_id):
    get_object_or_404(Questao, pk=questao_id).delete()
    return HttpResponseRedirect(reverse('votacao:index'))


@user_passes_test(check_superuser, login_url=reverse_lazy('votacao:detalhe'))
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


@user_passes_test(check_superuser, login_url=reverse_lazy('votacao:detalhe'))
def remover_opcao(request, opcao_id, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    get_object_or_404(Opcao, pk=opcao_id).delete()
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


@login_required(login_url=reverse_lazy('votacao:login'))
def info_pessoal(request):
    username = request.user.username
    email = request.user.email
    data = request.user.date_joined
    u = Aluno.objects.get(user_id=request.user.id)
    curso = u.curso
    votos = u.votos
    avatar = u.avatar
    return render(request, 'votacao/info_pessoal.html', {'username': username, 'email': email,
                                                         'data': data, 'curso': curso, 'votos': votos,
                                                         'avatar': avatar})


@login_required(login_url=reverse_lazy('votacao:login'))
def fazer_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        username = request.user.username
        email = request.user.email
        data = request.user.date_joined
        u = Aluno.objects.get(user_id=request.user.id)
        curso = u.curso
        votos = u.votos
        u.avatar = uploaded_file_url
        u.save()
        return render(request, 'votacao/info_pessoal.html', {'uploaded_file_url': uploaded_file_url,
                                                             'username': username, 'email': email,
                                                             'data': data, 'curso': curso, 'votos': votos,
                                                             'avatar': u.avatar})
    return render(request, 'votacao/info_pessoal.html')
