import sqlite3 as connector

conexao = connector.connect(r"C:/EAD/banco_de_dados/meu_banco.db")
cursor = conexao.cursor()

comando = '''ALTER TABLE Veiculo
                ADD motor REAL'''

cursor.execute(comando)

conexao.commit

cursor.close
conexao.close