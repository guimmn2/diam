import sqlite3
from votacao.models import Questao, Opcao

try:
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute("SELECT Sum(votos) FROM votacao_opcao")
    totalVotos = cursor.fetchone()
    print("Alinea a) Total de votos: " + str(totalVotos[0]))
    cursor.execute('''SELECT questao_texto, opcao_texto, MAX(votos)
                   FROM votacao_questao INNER JOIN votacao_opcao ON votacao_questao.id = questao_id
                   GROUP BY questao_texto''')
    result = cursor.fetchall()
    print("Alinea b)")
    for res in result:
        print(res)

    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if conn:
        conn.close()
        print("The SQLite connection is closed")
