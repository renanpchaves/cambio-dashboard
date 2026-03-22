from fastapi import FastAPI
import requests

app = FastAPI(
    title="Câmbio - Dashboard API",
    description="API para consulta de cotação USD-BRL",
    version="0.1.0" #beta
)

@app.get("/")
def root():
    """
    Endpoint root da API.

    Informações básicas.
    """
    return{
        "message": "API de câmbio rodando",
        "docs_interativo": "/docs"
    }

@app.get("/exchange/usd-brl")
def get_usd_brl():
    """
    Retorna cotação atual USD em relação ao BRL, consumindo awesomeAPI.

    1. Requisição HTTP para API externa
    2. Valida se a resposta foi ok
    3. Extrai dados relevantes
    4. Retorna um JSON para o cliente
    """

    url = ('https://economia.awesomeapi.com.br/last/USD-BRL')
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    usd = data["USDBRL"]

    return {
        "code": usd["code"], #código base (USD)
        "codein": usd["codein"], #código da moeda de destino (BRL)
        "name": usd["name"], #nome completo do par de moedas
        "bid": usd["bid"], #preço de compra (quanto o mercado paga)
        "ask": usd["ask"], #preço de venda (quanto o mercado cobra)
        "high": usd["high"], #maior valor do dia
        "low": usd["low"], #menor valor do dia
        "pctChange": usd["pctChange"], #variação em % no dia
        "timestamp": usd["timestamp"], #timestamp Unix da cotação
        "create_date": usd["create_date"] #data/hora formatada da cotação
    }