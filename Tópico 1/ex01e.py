# Implemente um programa que tenha como entrada o valor em uma reais e mostre o valor correspondente em dólar.
import requests

URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
response = requests.get(URL).json()
COTACAO = float(response.get('USDBRL').get('bid'))

valor_real = float(input("Real: R$"))
valor_dolar = valor_real / COTACAO

print(f"Valor em dólar: ${round(valor_dolar, 2)}")
