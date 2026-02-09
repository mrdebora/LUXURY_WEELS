import pandas as pd
import sqlite3
import logging
import pytest

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_financial_data(file_path):
    try:
        # extração
        df = pd.read_csv(file_path)
        logging.info("Dados extraídos com sucesso.")

        #transformçao(transações acima de 1000€)
        df_filtered = df[df['amount'] > 1000]
        df_filtered['status'] = 'High Value'
        logging.info("Dados transformados com sucesso.")


        # carregamento
        conn = sqlite3.connect('financial_data.db')
        df_filtered.to_sql('transactions', conn, if_exists='replace', index=False)
        conn.close()

        logging.info(f"Processadas {len(df_filtered)} linhas para a base de dados")
        return df_filtered
    except Exception as e:
        logging.error(f"erro no pipeline: {e}")
        return None

if __name__ == '__main__':
    process_financial_data('transactions.csv')


# A função a ser testada (ex: calculador de impostos simples)
def calculate_tax(amount, rate=0.23):
    if amount < 0:
        raise ValueError("O valor não pode ser negativo")
    return round(amount * rate, 2)
#Testes Automatizados (Pytest)

# O Teste (Usando pytest)
def test_calculate_tax_success():
    assert calculate_tax(100, 0.23) == 23.0
    assert calculate_tax(1000, 0.10) == 100.0

def test_calculate_tax_negative_value():
    with pytest.raises(ValueError):
        calculate_tax(-50)

#Integração com APIs e JSON

import requests

def get_exchange_rates(base_currency="EUR"):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Extrair apenas o que interessa (ex: USD e GBP)
        rates = {
            "USD": data['rates'].get('USD'),
            "GBP": data['rates'].get('GBP')
        }
        return rates
    else:
        print(f"Erro na API: {response.status_code}")
        return None

# O que explicar: "Usei o requests para consumo e tratei o status code
# para garantir que o serviço estava disponível antes de processar o JSON."

