#7- Como executar uma consulta SELECT simples?

import cursor1
import conexao

cursor1.execute("SELECT * FROM usuarios")
resultados = cursor1.fetchall()

for linha in resultados:
  print(linha)

conexao.close()