import sqlite3 as connector

# Abertura de conexão
conexao = connector.connect("URL SQLite")

# Aquisição de um cursor
cursor = conexao.cursor()

# Execução comandos: SELECT, CREATE, etc...
cursor.execute("SELECT * from ...")
cursor.fetchall()

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()