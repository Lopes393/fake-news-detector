async function analyzeNews() {

    const text = document.getElementById("news").value;

    if(text.trim() === "") {
        alert("Digite uma notícia.");
        return;
    }

    const resultDiv = document.getElementById("result");

    resultDiv.innerHTML = "Analisando com IA...";

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    text: text
                })
            }
        );

        const data = await response.json();

        if(data.error) {

            resultDiv.innerHTML = `
                <p>Erro:</p>
                <p>${data.error}</p>
            `;

            return;
        }

        resultDiv.innerHTML = `
            <h2>${data.result}</h2>

            <p>
                Fake News:
                ${data.fake_probability}%
            </p>

            <p>
                Notícia Real:
                ${data.true_probability}%
            </p>

            <p>
                <strong>Explicação:</strong><br>
                ${data.explanation}
            </p>
        `;

    } catch(error) {

        console.error(error);

        resultDiv.innerHTML = `
            Erro ao conectar com a API.
        `;
    }
}