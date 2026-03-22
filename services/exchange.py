import requests

class ExchangeService:
    BASE_URL = "https://economia.awesomeapi.com.br"

    def get_usd_brl(self):
        """
        Busca a cotação USD-BRL na awesomeAPI e retorna dados formatados.
        """
        url = f"{self.BASE_URL}/last/USD-BRL"

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        usd = data["USDBRL"]

        return {
            "code": usd["code"], #código base (USD)
            "codein": usd["codein"], #código da moeda de destino (BRL)
            "name": usd["name"], #nome completo do par de moedas
            "bid": float(usd["bid"]), #preço de compra (quanto o mercado paga)
            "ask": float(usd["ask"]), #preço de venda (quanto o mercado cobra)
            "high": float(usd["high"]), #maior valor do dia
            "low": float(usd["low"]), #menor valor do dia
            "pctChange": float(usd["pctChange"]), #variação em % no dia
            "timestamp": usd["timestamp"], #timestamp Unix da cotação
            "create_date": usd["create_date"] #data/hora formatada da cotação
        }

#INSTANCIA DO SERVIÇO:
exchange_service = ExchangeService()