clientes = [
    {'nome': 'Ana', 'saldo': 1500 , 'idade':28}, 
    {'nome': 'Debora', 'saldo': 450 , 'idade':30}, 
    {'nome': 'Luis', 'saldo': 5000, 'idade':35}
]

print("Clientes com saldo inferior a 1000€:")
print("-" * 40)

for cliente in clientes:
    if cliente['saldo'] < 1000:
        print(f"Nome: {cliente['nome']} - Saldo: {cliente['saldo']}€")

        
print("Clientes com saldo superior a 1000€:")
print("-" * 40)

for cliente in clientes:
    if cliente['saldo'] > 1000:
        print(f"Nome: {cliente['nome']} - Saldo: {cliente['saldo']}€")


print("Clientes com idade superior a 30 anos:")
print("-" * 40) 

for cliente in clientes:
    if cliente['idade'] >= 30:
        print(f"Nome: {cliente['nome']} - Idade: {cliente['idade']} anos")