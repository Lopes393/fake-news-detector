from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv

import os
import json

# Carregar variáveis do .env
load_dotenv()

# Criar app Flask
app = Flask(__name__)

# Liberar CORS
CORS(app)

# Cliente OpenAI
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.route("/")
def home():
    return "API Detector de Fake News com ChatGPT funcionando!"

@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        text = data["text"]

        prompt = f"""
        Você é um especialista em análise de fake news.

        Analise a notícia abaixo.

        Considere:
        - plausibilidade
        - coerência
        - contexto atual
        - linguagem alarmista
        - ausência de fontes
        - exageros
        - sensacionalismo

        Retorne APENAS um JSON válido neste formato:

        {{
            "result": "Fake News" ou "Provavelmente Real",
            "fake_probability": número de 0 a 100,
            "true_probability": número de 0 a 100,
            "explanation": "explicação curta"
        }}

        Notícia:
        {text}
        """

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        content = response.choices[0].message.content

        # Converter resposta para JSON
        result = json.loads(content)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)