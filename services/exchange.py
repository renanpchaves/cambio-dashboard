import requests
from fastapi import HTTPException

class ExchangeService:
    BASE_URL = "https://economia.awesomeapi.com.br"

    def get_usd_brl(self):
        """
        Busca a cotação USD-BRL na awesomeAPI e retorna dados formatados.
        """
        try:
            url = f"{self.BASE_URL}/last/USD-BRL"
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()
            usd = data.get("USDBRL")
            if not usd:
                raise HTTPException (status_code=502,detail=f'Resposta inválida da API externa.')

            return {
                "code": usd["code"], #código base (USD)
                "codein": usd["codein"], #código da moeda de destino (BRL)
                "name": usd["name"], #nome completo do par de moedas
                "bid": f"R$ {float(usd["bid"]):.2f}", #preço de compra (quanto o mercado paga)
                "ask": f"R$ {float(usd["ask"]):.2f}", #preço de venda (quanto o mercado cobra)
                "high": f"R$ {float(usd["high"]):.2f}", #maior valor do dia
                "low": f"R$ {float(usd["low"]):.2f}", #menor valor do dia
                "pctChange": f"{float(usd["pctChange"]):.3f}", #variação em % no dia
                "timestamp": int(usd["timestamp"]), #timestamp Unix da cotação
                "create_date": usd["create_date"] #data/hora formatada da cotação
            }
        except requests.exceptions.HTTPError as e:
            raise HTTPException(status_code=502,detail=f'Erro ao consumir API externa: {e}')
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=503,detail=f'Serviço temporariamente indisponível: {e}')
        except KeyError as e:
            raise HTTPException(status_code=500, detail=f'Resposta inesperada da API: {e}')

#INSTANCIA DO SERVIÇO:
exchange_service = ExchangeService()