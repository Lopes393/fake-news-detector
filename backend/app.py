from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Carregar IA treinada
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return "API Detector de Fake News funcionando!"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json
    text = data["text"]

    # Transformar texto
    vectorized_text = vectorizer.transform([text])

    # Fazer previsão
    prediction = model.predict(vectorized_text)[0]
    probability = model.predict_proba(vectorized_text)[0]

    fake_probability = probability[0] * 100
    true_probability = probability[1] * 100

    return jsonify({
        "fake_probability": round(fake_probability, 2),
        "true_probability": round(true_probability, 2),
        "result": "Fake News" if prediction == 0 else "Notícia Real"
    })

if __name__ == "__main__":
    app.run(debug=True)