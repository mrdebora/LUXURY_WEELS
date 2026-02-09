import pandas as pd

# Criação do DataFrame de transações
df_transacoes = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'cliente': ['Ana', 'João', 'Maria', 'Pedro', 'Carla', 'Luis', 'Sofia', 'Miguel', 'Beatriz', 'Rui'],
    'valor': [150.50, 230.00, 89.90, 450.00, 125.75, 670.00, 55.30, 310.00, 95.60, 420.50],
    'tipo': ['Débito', 'Crédito', 'Débito', 'Crédito', 'Débito', 'Crédito', 'Débito', 'Crédito', 'Débito', 'Crédito']
})

print("=" * 50)
print("ANÁLISE DE TRANSAÇÕES BANCÁRIAS")
print("=" * 50)

# Verificar as primeiras 5 linhas
print("\n📊 Primeiras 5 linhas do DataFrame:")
print(df_transacoes.head())

# Calcular a média da coluna "valor"
media_valor = df_transacoes['valor'].mean()
print(f"\n💰 Média dos valores das transações: {media_valor:.2f}€")

# Informações adicionais úteis
print(f"\n📈 Informações adicionais:")
print(f"   - Total de transações: {len(df_transacoes)}")
print(f"   - Valor total: {df_transacoes['valor'].sum():.2f}€")
print(f"   - Valor mínimo: {df_transacoes['valor'].min():.2f}€")
print(f"   - Valor máximo: {df_transacoes['valor'].max():.2f}€")
