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
    document.getElementById("create_date").textContent = data.create_date;

    console.log(data);
}   catch (error) {
        console.error("Erro ao buscar cotação:", error)
    }
}

loadExchange()