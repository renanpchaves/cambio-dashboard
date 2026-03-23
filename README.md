# 💱 Câmbio Dashboard

Dashboard simples para visualização da cotação USD → BRL em tempo real, utilizando FastAPI no backend e JavaScript no frontend.

---

## 🚀 Funcionalidades

* Consulta de cotação USD-BRL em tempo real
* Exibição de:
  * Preço de compra e venda
  * Máxima e mínima do dia
  * Variação percentual
  * Data da última atualização
* Atualização manual via botão

---

## 🛠️ Tecnologias

* **Backend:** Python + FastAPI
* **Frontend:** HTML, CSS e JavaScript
* **API externa:** AwesomeAPI (cotações de moedas)

---

## 📁 Estrutura do projeto

```
cambio-dashboard/
├── main.py
├── README.md
├── services/
│   └── exchange.py
└── frontend/
    ├── index.html
    ├── style.css
    └── script.js
```

---

## ⚙️ Como rodar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/cambio-dashboard.git
cd cambio-dashboard
```

---

### 2. Criar ambiente virtual (opcional)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Rodar o backend

```bash
python main.py
```

A API estará disponível em:

```
http://localhost:8000
```

---

### 5. Rodar o frontend e visualizar os dados

Abra o arquivo `frontend/index.html` com um servidor local (ex: Live Server no VS Code).

---