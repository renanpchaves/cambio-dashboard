//Função principal de captura dos dados do back-end
let currentCurrency = "USD";
let currentIndex = 0;

async function loadExchange(currency = "USD") {
  try {
    const response = await fetch(
      `http://localhost:8000/exchange/cotacao/${currency.toLowerCase()}`,
    );

    if (!response.ok) {
      throw new Error("Erro na requisição!");
    }

    //buscando os dados na API* por campo:
    const data = await response.json();
    document.getElementById("name").textContent = data.name;
    document.getElementById("bid").textContent = data.bid;
    document.getElementById("ask").textContent = data.ask;
    document.getElementById("high").textContent = data.high;
    document.getElementById("low").textContent = data.low;
    document.getElementById("pctChange").textContent = data.pctChange + "%";
    document.getElementById("create_date").textContent = formatarData(
      data.create_date,
    );
    document.getElementById("currency-label").textContent =
      currency.toUpperCase();

    console.log(data);
  } catch (error) {
    console.error("Erro ao buscar cotação:", error);
  }
}

//formatando data para ptBR, deixando mais legível
const formatarData = (dataISO) => {
  const data = new Date(dataISO);
  return data
    .toLocaleString("pt-BR", {
      day: "2-digit",
      month: "2-digit",
      year: "numeric",
      hour: "2-digit",
      minute: "2-digit",
    })
    .replace(",", " -");
};

//função para troca de moeda, configurando o carrossel:
function switchCurrency(direction) {
  const currencies = ["USD", "EUR"];
  const card = document.querySelector(".card");

  //Fadeout
  card.classList.remove("active");

  setTimeout(() => {
    if (direction === "next") {
      currentIndex = (currentIndex + 1) % currencies.length;
    } else {
      currentIndex =
        currentIndex(currentIndex - 1 + currencies.length) % currencies.length;
    }
    currentCurrency = currencies[currentIndex];

    //Carrega novos dados
    loadExchange(currentCurrency);

    //Fadein
    setTimeout(() => {
      card.classList.add("active");
    }, 50);
  }, 400);
}

//Load dados iniciais
loadExchange(currentCurrency);

//CARD no carregamento inicial:
document.querySelector(".card").classList.add("active");

//atualizando a Dashboard
document.getElementById("refreshButton").addEventListener("click", () => {
  loadExchange(currentCurrency);
});

// Botões de navegação do carrossel
document.getElementById("prevButton").addEventListener("click", () => {
  switchCurrency("prev");
});

document.getElementById("nextButton").addEventListener("click", () => {
  switchCurrency("next");
});
