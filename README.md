#  Python e BD - Atividad de Pesquisa Sobre Bibliotecas Python para Conexão com Bancos de Dados

Pesquisa sobre bibliotecas Python para conexão com bancos de dados

Aqui falarei sobre sqlite3 e sobre pyodbc

Primeiro Tema  SQLITE3

1- Qual é o objetivo principal da biblioteca?
O objetivo principal do sqlite3 é fornecer uma interface leve, integrada e autossuficiente compatível com a especificação DB-API 2.0 (PEP 249) para interagir com bancos de dados SQLite.

2- Que tipo de banco de dados ela permite acessar?
Bancos de dados SQLite (bancos de dados baseados em arquivos locais, sem a necessidade de um servidor de banco de dados separado).

3- Ela é mais indicada para bancos relacionais ou não relacionais?
Relacionais (SQL).

4- A biblioteca trabalha com SQL puro, ORM ou ambos?
Trabalha estritamente com SQL puro.

5- Como é feita a instalação?
O sqlite3 já vem pré-instalado por padrão na biblioteca padrão do Python

6- Como é criado um exemplo simples de conexão? Resposta em Código na pasta SQLITE3
7- Como executar uma consulta *SELECT* simples? Resposta em Código na pasta SQLITE3


Segundo Tema PYODBC

1- Qual é o objetivo principal da biblioteca?
Permitir o acesso a bancos de dados usando conexões ODBC (Open Database Connectivity), permitindo que aplicativos Python se conectem a praticamente qualquer SGBD que possua um driver ODBC instalado no sistema operacional.

2- Que tipo de banco de dados ela permite acessar?
Vários bancos de dados relacionais que suportam ODBC (SQL Server, PostgreSQL, Oracle, MySQL, Access, etc.). É muito utilizada para Microsoft SQL Server no ecossistema Windows.

3- Ela é mais indicada para bancos relacionais ou não relacionais?
Relacionais (SQL).

4- A biblioteca trabalha com SQL puro, ORM ou ambos?
Trabalha com SQL puro.

5- Como é feita a instalação?
Via pip (exige que os drivers ODBC estejam configurados no S.O.):

Bash
pip instal pyodbc

6- Como é criado um exemplo simples de conexão? Resposta em Código na pasta PYODBC
7- Como executar uma consulta *SELECT* simples? Resposta em Código na pasta PYODBC
