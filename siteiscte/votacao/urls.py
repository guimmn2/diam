from django.urls import path

from . import views

app_name = 'votacao'
urlpatterns = [
    # ex: votacao/
    path("", views.index, name='index'),
    # ex: votacao/1
    path('<int:questao_id>', views.detalhe, name='detalhe'),
    # ex: votacao/5/voto
    path('<int:questao_id>/voto', views.voto, name='voto'),
    path('criarquestao', views.criarquestao, name='criarquestao'),
    path('<int:questao_id>/criaropcao', views.criaropcao, name="criaropcao"),
    path('registar', views.registar, name="registar"),
    path('login', views.loginview, name="login"),
    path('logout', views.logoutview, name="logout"),
    path('info_pessoal', views.info_pessoal, name="info_pessoal"),
    path('<int:questao_id>, remover_questao', views.remover_questao, name="remover_questao"),
    path('<int:opcao_id>, <int:questao_id>, remover_opcao', views.remover_opcao, name="remover_opcao"),
    path('fazer_upload', views.fazer_upload, name='fazer_upload'),
    path('api/questoes/', views.questoes_lista),
    path('api/questoes/<int:pk>', views.questoes_edita),
    path('api/opcoes/', views.opcoes_lista),
    path('api/opcoes/<int:pk>', views.opcoes_edita),

]
