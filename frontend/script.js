//Função principal de captura dos dados do back-end
async function loadExchange() {
    try{
    const response = await fetch("http://localhost:8000/exchange/cotacao");

    if (!response.ok) {
        throw new Error("Erro na requisição!");
    }

    const data = await response.json()
    document.getElementById("name").textContent = data.name;
    document.getElementById("bid").textContent = data.bid;
    document.getElementById("ask").textContent = data.ask;
    document.getElementById("high").textContent = data.high;
    document.getElementById("low").textContent = data.low;
    document.getElementById("pctChange").textContent = data.pctChange + "%";
    document.getElementById("create_date").textContent = formatarData(data.create_date);

    console.log(data);
}   catch (error) {
        console.error("Erro ao buscar cotação:", error)
    }
}

//formatando data para ptBR
const formatarData = (dataISO) => {
    const data = new Date(dataISO);
    return data.toLocaleString('pt-BR', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
    }).replace(',',' -');
};

loadExchange()