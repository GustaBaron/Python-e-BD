# 6- Como é criado um exemplo simples de conexão?

import sqlite3

# Conecta a um banco de dados local (cria o arquivo se não existir)
conexao = sqlite3.connect("meu_banco.db")
cursor1 = conexao.cursor()