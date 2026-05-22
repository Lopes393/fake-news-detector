async function analyzeNews() {

    const text = document.getElementById("news").value;

    if(text.trim() === "") {
        alert("Digite uma notícia.");
        return;
    }

    const resultDiv = document.getElementById("result");

    resultDiv.innerHTML = "Analisando...";

    try {

        const response = await fetch("http://127.0.0.1:5000/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                text: text
            })
        });

        const data = await response.json();

        resultDiv.innerHTML = `
            <p>${data.result}</p>

            <p>Fake News: ${data.fake_probability}%</p>

            <p>Notícia Real: ${data.true_probability}%</p>
        `;

    } catch(error) {

        resultDiv.innerHTML = `
            Erro ao conectar com a API.
        `;

        console.error(error);
    }
}