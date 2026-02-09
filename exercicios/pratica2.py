import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE Clientes (
    id_cliente INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT
)
''')


cursor.execute('''
CREATE TABLE Emprestimos (
    id_emprestimo INTEGER PRIMARY KEY,
    id_cliente INTEGER,
    valor REAL NOT NULL,
    data_emprestimo TEXT,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
)
''')

clientes = [
    (1, 'Ana Silva', 'ana.silva@email.com'),
    (2, 'João Costa', 'joao.costa@email.com'),
    (3, 'Maria Santos', 'maria.santos@email.com'),
    (4, 'Pedro Oliveira', 'pedro.oliveira@email.com'),
    (5, 'Carla Ferreira', 'carla.ferreira@email.com')
]
cursor.executemany('INSERT INTO Clientes VALUES (?, ?, ?)', clientes)


emprestimos = [
    (1, 1, 15000.00, '2024-01-15'),
    (2, 2, 25000.00, '2024-02-20'),
    (3, 1, 8000.00, '2024-03-10'),
    (4, 4, 50000.00, '2024-04-05'),
    (5, 3, 12000.00, '2024-05-12')
]
cursor.executemany('INSERT INTO Emprestimos VALUES (?, ?, ?, ?)', emprestimos)

conn.commit()

print("=" * 60)
print("SQL INNER JOIN - CLIENTES E EMPRÉSTIMOS")
print("=" * 60)

# Query com INNER JOIN para listar nome do cliente e valor do empréstimo
query = '''
SELECT Clientes.nome, Emprestimos.valor 
FROM Clientes 
INNER JOIN Emprestimos 
ON Clientes.id_cliente = Emprestimos.id_cliente
'''

print("\n📝 Query SQL:")
print(query)

# Executar a query
cursor.execute(query)
resultados = cursor.fetchall()

print("\n📊 Resultados:")
print("-" * 60)
print(f"{'Nome do Cliente':<25} {'Valor do Empréstimo (€)':>20}")
print("-" * 60)

for nome, valor in resultados:
    print(f"{nome:<25} {valor:>20,.2f}€")

print("-" * 60)
print(f"Total de empréstimos: {len(resultados)}")

# Query adicional: Total de empréstimos por cliente
print("\n\n💰 Total de Empréstimos por Cliente:")
print("-" * 60)
query_total = '''
SELECT Clientes.nome, COUNT(Emprestimos.id_emprestimo) as num_emprestimos, 
       SUM(Emprestimos.valor) as total_emprestado
FROM Clientes 
INNER JOIN Emprestimos 
ON Clientes.id_cliente = Emprestimos.id_cliente
GROUP BY Clientes.id_cliente, Clientes.nome
'''

cursor.execute(query_total)
totais = cursor.fetchall()

print(f"{'Cliente':<20} {'Nº Empréstimos':>15} {'Total (€)':>20}")
print("-" * 60)
for nome, num, total in totais:
    print(f"{nome:<20} {num:>15} {total:>20,.2f}€")

conn.close()

print("\n" + "=" * 60)
print("✅ Conceito aplicado: INNER JOIN para relacionar tabelas")
print("=" * 60)
