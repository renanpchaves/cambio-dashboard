from fastapi import FastAPI, HTTPException
from services.exchange import (
    exchange_service
    )
import requests
from fastapi.middleware.cors import CORSMiddleware

# =================================================
# CONFIG DA APLICAÇÃO
# =================================================

app = FastAPI(
    title="Câmbio - Dashboard API",
    description="API para consulta de cotação USD-BRL",
    version="0.1.0" #beta
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],  #front eventualmente?
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# =================================================
# ENDPOINTS
# =================================================

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

@app.get("/exchange/cotacao")
def get_usd_brl():
    """
    Retorna cotação atual USD em relação ao BRL, consumindo awesomeAPI.

    1. Requisição HTTP para API externa
    2. Valida se a resposta foi ok
    3. Extrai dados relevantes
    4. Retorna um JSON para o cliente
    """
    try:
        return exchange_service.get_usd_brl()
    except requests.RequestException as e:
        raise HTTPException(
            status_code=502,
            detail=f"Erro ao consultar a API externa: {str(e)}"
        )
        
# =================================================
# MAIN
# =================================================

if __name__ == "__main__":
    import uvicorn

    print("""
    ╔════════════════════════════════════════════╗
    ║  Cambio Dashboard                          ║
    ║                                            ║
    ║  📖 Docs: http://localhost:8000/docs       ║
    ╚════════════════════════════════════════════╝
    """)

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )