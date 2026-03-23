async function loadExchange() {
    try{
    const response = await fetch("http://localhost:8000/exchange/cotacao");

    if (!response.ok) {
        throw new Error("Erro na requisição!");
    }

    const data = await response.json()

    console.log(data);
}   catch (error) {
        console.error("Erro ao buscar cotação:", error)
    }
}

loadExchange()