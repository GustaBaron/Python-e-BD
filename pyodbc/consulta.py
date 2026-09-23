# 7- Como executar uma consulta SELECT simples?

import cursor
import conexao

cursor.execute("SELECT * FROM usuarios")
for linha in cursor.fetchall():
  print(linha)

conexao.close()