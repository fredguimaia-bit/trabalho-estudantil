#exibição de vendas

import sqlite3

conexao = sqlite3.connect('dados_vendas.db')
cursor = conexao.cursor()

cursor.execute('DROP TABLE IF EXISTS vendas1')

create_table = """
CREATE TABLE vendas1 (
  id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
  data_venda DATE NOT NULL,
  produto TEXT NOT NULL,
  categoria TEXT NOT NULL,
  valor_venda REAL NOT NULL)
"""
cursor.execute(create_table)
conexao.commit() # Corrigido de conn.commit() para conexao.commit()

# Dados a serem inseridos
dados_vendas = [
    ('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
    ('2023-01-05', 'Produto B', 'Roupas', 350.00),
    ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
    ('2023-03-15', 'Produto D', 'Livros', 200.00),
    ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
    ('2023-04-02', 'Produto F', 'Roupas', 400.00),
    ('2023-05-05', 'Produto G', 'Livros', 150.00),
    ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
    ('2023-07-20', 'Produto I', 'Roupas', 600.00),
    ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
    ('2023-09-30', 'Produto K', 'Livros', 300.00),
    ('2023-10-05', 'Produto L', 'Roupas', 450.00),
    ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
    ('2023-12-20', 'Produto N', 'Livros', 250.00)
]

cursor.executemany("INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES (?, ?, ?, ?)", dados_vendas)

conexao.commit()
cursor.close()
conexao.close()

print(dados_vendas)

#criaçao da tabela em panda
import pandas as pd
import sqlite3
conexao = sqlite3.connect('dados_vendas.db')
cursor = conexao.cursor()

df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)
conexao.close()

df_vendas.head()

#tabela visual de vendas
df_vendas.columns = ["id", "data", "produto", "categoria", "venda"]
print(df_vendas)

print(f"---------------------------------------------------------------")
print("MÉDIA DE VENDAS:",df_vendas.venda.mean().round(2))
print(f"---------------------------------------------------------------")
print("TOTAL DE VENDAS:",df_vendas.venda.sum())
print(f"---------------------------------------------------------------")
print("VENDA MÁXIMA:",df_vendas.venda.max())
print(f"---------------------------------------------------------------")
print("VENDA MÍNIMA:",df_vendas.venda.min())

#Gráficos
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_vendas['data'] = pd.to_datetime(df_vendas['data'])
df_vendas.set_index('data', inplace=True)
df_vendas['venda'].plot(figsize=(12, 6))
plt.title('Vendas ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Valor da Venda')
plt.show()
