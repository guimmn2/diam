from aifc import Error

from votacao.models import Questao, Opcao
from django.db import models
from django.utils import timezone
from six import string_types
from django.db.models import F
import datetime
import sqlite3

## Estabelecer conexão

conn = sqlite3.connect(r"db.sqlite3")

## Criar cursor (a ponte entre o SQLite e a SQLQuery)
print("\nAlinea a)")
with conn:

    ## alínea a)
    cur = conn.cursor()
    cur.execute("SELECT SUM(votos) FROM votacao_opcao")

    rows = cur.fetchall()

    for row in rows:
        print("Numero total de votos: " + str(row[0]))

    ## alínea b)
    ##cur.execute("SELECT questao_texto, opcao_texto, votos FROM votacao_questao, votacao_opcao WHERE votacao_questao.id=votacao_opcao.questao_id")

    ##cur.execute("SELECT vq.questao_texto, va.opcao_texto, va.votos "
    ##            "FROM votacao_opcao AS vo JOIN votacao_questao AS vq ON va.questao_id =  vq.id"
    ##            "WHERE vo.id IN (SELECT id FROM votacao_opcao WHERE )")

    print("\nAlinea b)")
    cur.execute("SELECT questao_texto, opcao_texto, MAX(votos) FROM votacao_questao, votacao_opcao WHERE votacao_questao.id = questao_id GROUP BY questao_id")

    rows = cur.fetchall()

    for row in rows:
        print(str(row[0:2]))