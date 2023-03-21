from django.urls import path

from . import views

app_name = 'votacao'
urlpatterns = [
    # ex: votacao/
    path("", views.index, name='index'),
    # ex: votacao/1
    path('<int:questao_id>', views.detalhe, name='detalhe'),
    # ex: votacao/3/resultados
    path('<int:questao_id>/resultados', views.resultados, name='resultados'),
    # ex: votacao/5/voto
    path('<int:questao_id>/voto', views.voto, name='voto'),
    path('criar_questao', views.criar_questao, name='criarquestao'),
    path('<int:questao_id>/guardar_questao', views.guardar_questao, name='guardarquestao'),
    path('criar_opcao', views.criar_opcao, name="criaropcao"),
    path('<int:questao_id>/guardar_opcao', views.guardar_opcao, name="guardaropcao"),
    path('registar', views.registar, name="registar"),
    path('guardar_registo', views.guardar_registo, name="guardar_registo"),
    path('login', views.loginview, name="login"),
    path('autenticacao', views.autenticacao, name="autenticacao"),
    path('logout', views.logoutview, name="logout"),
    path('info_pessoal', views.info_pessoal, name="info_pessoal")
]
