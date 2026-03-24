import requests
from fastapi import HTTPException

class ExchangeService:
    BASE_URL = "https://economia.awesomeapi.com.br"

    def get_exchange_rate(self, currency: str = "USD"):
        """
        Busca a cotação USD-BRL na awesomeAPI e retorna dados formatados.

        Args:
            currency (str): Código da moeda (USD, EUR, GBP, etc.)

            returns:
            dict: Dados formatados da cotação
        """
        try:
            pair = f"{currency}-BRL"
            url = f"{self.BASE_URL}/last/{pair}"

            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()

            key = pair.replace("-","")
            exchange_data = data.get(key)

            if not exchange_data:
                raise HTTPException (status_code=502,detail=f'Resposta inválida da API externa para: {pair}')

            return {
                "code": exchange_data["code"], #código base (USD)
                "codein": exchange_data["codein"], #código da moeda de destino (BRL)
                "name": exchange_data["name"], #nome completo do par de moedas
                "bid": f"R$ {float(exchange_data["bid"]):.2f}", #preço de compra (quanto o mercado paga)
                "ask": f"R$ {float(exchange_data["ask"]):.2f}", #preço de venda (quanto o mercado cobra)
                "high": f"R$ {float(exchange_data["high"]):.2f}", #maior valor do dia
                "low": f"R$ {float(exchange_data["low"]):.2f}", #menor valor do dia
                "pctChange": f"{float(exchange_data["pctChange"]):.3f}", #variação em % no dia
                "timestamp": int(exchange_data["timestamp"]), #timestamp Unix da cotação
                "create_date": exchange_data["create_date"] #data/hora formatada da cotação
            }
        except requests.exceptions.HTTPError as e:
            raise HTTPException(status_code=502,detail=f'Erro ao consumir API externa: {e}')
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=503,detail=f'Serviço temporariamente indisponível: {e}')
        except KeyError as e:
            raise HTTPException(status_code=500, detail=f'Resposta inesperada da API: {e}')


    def get_usd_brl(self):
        """
        Busca cotação USD-BRL
        """
        return self.get_exchange_rate("USD")
    def get_eur_brl(self):
        """
        Busca cotação EUR-BRL
        """
        return self.get_exchange_rate("EUR")
    
#INSTANCIA DO SERVIÇO:
exchange_service = ExchangeService()