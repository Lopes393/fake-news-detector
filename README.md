# Detector de Fake News com Inteligência Artificial

Sistema desenvolvido para análise automática de notícias utilizando Machine Learning, capaz de identificar a probabilidade de uma notícia ser falsa (Fake News) ou verdadeira.

---

# Objetivo do Projeto

O projeto tem como objetivo demonstrar o uso de:

- Inteligência Artificial
- Machine Learning
- Processamento de Linguagem Natural (NLP)
- Desenvolvimento Web
- Ciência de Dados

aplicados na detecção de notícias falsas.

O sistema recebe um texto digitado pelo usuário, analisa padrões linguísticos e retorna a probabilidade da notícia ser falsa ou verdadeira.

---

# Tecnologias Utilizadas

## Back-end
- Python
- Flask

## Inteligência Artificial
- Scikit-Learn
- TF-IDF
- Logistic Regression

## Front-end
- HTML5
- CSS3
- JavaScript

## Banco de Dados (Opcional)
- SQLite
- MySQL

---

# Funcionalidades

- Análise de notícias em tempo real
- Identificação de Fake News
- Cálculo de probabilidade
- API REST
- Interface Web simples e intuitiva
- Treinamento de modelo de IA

---

# Estrutura do Projeto

```text
fake-news-detector/
│
├── backend/
│   ├── app.py
│   ├── train.py
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── dataset/
│   ├── Fake.csv
│   └── True.csv
│
├── requirements.txt
└── README.md
```

---

# Como Funciona

## Fluxo do Sistema

```text
Usuário envia notícia
↓
Texto é processado
↓
IA transforma texto em dados numéricos
↓
Modelo analisa padrões
↓
Sistema retorna probabilidade
```

---

# Dataset Utilizado

O modelo foi treinado utilizando datasets públicos contendo notícias reais e falsas.

## Dataset
- Fake.csv
- True.csv

Fonte:
https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

---

# Instalação do Projeto

## 1. Clonar Repositório

```bash
git clone https://github.com/seu-usuario/fake-news-detector.git
```

---

## 2. Entrar na Pasta

```bash
cd fake-news-detector
```

---

## 3. Criar Ambiente Virtual

### Windows

```bash
python -m venv venv
```

---

## 4. Ativar Ambiente Virtual

### Windows

```bash
venv\Scripts\activate
```

---

## 5. Instalar Dependências

```bash
pip install -r requirements.txt
```

---

# Dependências do Projeto

## requirements.txt

```txt
pandas
numpy
scikit-learn
flask
```

---

# Treinamento da Inteligência Artificial

Entre na pasta backend:

```bash
cd backend
```

Execute:

```bash
python train.py
```

---

# Resultado Esperado

O terminal deverá exibir:

```text
Acurácia: 98.xx%
```

Além disso, serão gerados:

```text
model.pkl
vectorizer.pkl
```

---

# Executando a API

Dentro da pasta backend:

```bash
python app.py
```

Servidor iniciado em:

```text
http://127.0.0.1:5000
```

---

# Exemplo de Requisição

## Endpoint

```text
POST /predict
```

## JSON Enviado

```json
{
  "text": "Texto da notícia aqui"
}
```

## Resposta

```json
{
  "fake_probability": 87.5,
  "true_probability": 12.5,
  "result": "Fake News"
}
```

---

# Inteligência Artificial Utilizada

## TF-IDF

Responsável por converter textos em dados numéricos.

---

## Logistic Regression

Modelo de Machine Learning utilizado para classificação das notícias.

---

# Código de Treinamento da IA

## train.py

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# Ler datasets
fake = pd.read_csv("../dataset/Fake.csv")
true = pd.read_csv("../dataset/True.csv")

# Criar labels
fake["label"] = 0
true["label"] = 1

# Juntar dados
data = pd.concat([fake, true])

# Pegar texto e labels
x = data["text"]
y = data["label"]

# Converter texto em números
vectorizer = TfidfVectorizer(stop_words='english')

x_vectorized = vectorizer.fit_transform(x)

# Dividir treino e teste
x_train, x_test, y_train, y_test = train_test_split(
    x_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

# Criar IA
model = LogisticRegression()

# Treinar IA
model.fit(x_train, y_train)

# Testar IA
predictions = model.predict(x_test)

accuracy = accuracy_score(y_test, predictions)

print(f"Acurácia: {accuracy * 100:.2f}%")

# Salvar modelo
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
```

---

# Código da API

## app.py

```python
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Carregar modelo
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json
    text = data["text"]

    vectorized_text = vectorizer.transform([text])

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
```

---

# Possíveis Melhorias Futuras

- Interface moderna com React ou Next.js
- Dashboard com gráficos
- Integração com APIs de notícias
- Análise automática de links
- Análise de imagens falsas
- Integração com WhatsApp
- Deploy em nuvem
- Uso de modelos BERT/Transformers

---

# Demonstração para Feira Científica

O projeto pode ser demonstrado em tempo real:

1. Usuário digita uma notícia
2. Sistema analisa automaticamente
3. IA exibe probabilidade de ser falsa

Sugestão:
- Comparar notícias reais e falsas ao vivo
- Criar desafio para visitantes tentarem enganar a IA

---

# Conceitos Aplicados

- Machine Learning
- Processamento de Linguagem Natural
- APIs REST
- Ciência de Dados
- Desenvolvimento Web
- Inteligência Artificial

---

# Autor

Desenvolvido por Murilo Lopes para fins educacionais, aprendizado de Inteligência Artificial e apresentação em feira científica.

---

# Licença

Este projeto é destinado para fins educacionais e acadêmicos.
