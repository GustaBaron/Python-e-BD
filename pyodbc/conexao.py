#6. Como é criado um exemplo simples de conexão?

import pyodbc

string_conexao = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=seu_servidor;"
    "DATABASE=seu_banco;"
    "UID=seu_usuario;"
    "PWD=sua_senha"
)
conexao = pyodbc.connect(string_conexao)
cursor = conexao.cursor()