# 🧠 Fake News Detector AI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-API-black?style=for-the-badge&logo=flask)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-green?style=for-the-badge&logo=openai)
![JavaScript](https://img.shields.io/badge/JavaScript-Frontend-yellow?style=for-the-badge&logo=javascript)
![HTML5](https://img.shields.io/badge/HTML5-Web-orange?style=for-the-badge&logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-Style-blue?style=for-the-badge&logo=css3)

### 🚨 Sistema Inteligente de Detecção de Fake News usando IA Generativa

Projeto desenvolvido para feiras científicas, apresentações tecnológicas, aprendizado de Inteligência Artificial e demonstrações de análise contextual usando modelos de linguagem avançados.

</div>

---

# 📌 Sobre o Projeto

O **Fake News Detector AI** é um sistema web capaz de analisar notícias e identificar a probabilidade de serem falsas ou verdadeiras utilizando Inteligência Artificial Generativa.

Diferente de modelos simples de Machine Learning tradicionais, este projeto utiliza:

✅ IA contextual  
✅ Análise semântica  
✅ Interpretação textual  
✅ Verificação de plausibilidade  
✅ Explicações automáticas  

---

# 🎯 Objetivos

- Demonstrar uso de IA Generativa
- Aplicar APIs modernas de IA
- Trabalhar com análise textual
- Criar uma API REST com Flask
- Desenvolver um sistema completo Full Stack
- Estudar detecção de Fake News
- Integrar Front-end + Back-end + IA

---

# 🖼️ Demonstração

## Entrada:

```text
Donald Trump é presidente dos Estados Unidos
```

## Resultado:

```text
✅ Provavelmente Real

🟢 Notícia Real: 92%
🔴 Fake News: 8%

📖 Explicação:
A afirmação é consistente com acontecimentos políticos recentes.
```

---

# 🚀 Tecnologias Utilizadas

## 🧠 Inteligência Artificial
- OpenAI API
- GPT-4o
- Processamento de Linguagem Natural (NLP)

## ⚙️ Back-end
- Python
- Flask
- Flask-CORS

## 🎨 Front-end
- HTML5
- CSS3
- JavaScript

## 🔐 Segurança
- Python Dotenv
- Variáveis de Ambiente

---

# 🏗️ Estrutura do Projeto

```text
fake-news-detector/
│
├── backend/
│   ├── app.py
│   ├── .env
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .gitignore
└── README.md
```

---

# 🧠 Como Funciona

```text
Usuário digita uma notícia
↓
Front-end envia texto para Flask
↓
Flask envia prompt para OpenAI
↓
GPT-4o analisa contexto
↓
Sistema retorna:
- Probabilidade Fake
- Probabilidade Real
- Explicação
```

---

# ✨ Funcionalidades

✅ Análise contextual de notícias  
✅ IA generativa integrada  
✅ Respostas em português  
✅ Explicação automática da análise  
✅ API REST  
✅ Interface web interativa  
✅ Comunicação Front-end + Back-end  
✅ Sistema pronto para expansão  

---

# 📦 Instalação do Projeto

## 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/fake-news-detector.git
```

---

## 2️⃣ Entrar na Pasta

```bash
cd fake-news-detector
```

---

## 3️⃣ Criar Ambiente Virtual

### Windows

```bash
python -m venv venv
```

---

## 4️⃣ Ativar Ambiente Virtual

### PowerShell

```powershell
venv\Scripts\activate
```

### CMD

```cmd
venv\Scripts\activate.bat
```

---

## 5️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

---

# 📄 requirements.txt

```txt
flask
flask-cors
openai
python-dotenv
```

---

# 🔑 Configurando API Key

## Criar arquivo `.env`

Dentro da pasta:

```text
backend/
```

Crie:

```text
.env
```

---

## Adicionar chave OpenAI

```env
OPENAI_API_KEY=sua-chave-aqui
```

---

# ⚠️ IMPORTANTE

Nunca envie:
- `.env`
- API Keys

para o GitHub.

---

# 🛡️ Configurar .gitignore

```gitignore
venv/
.env
__pycache__/
```

---

# ▶️ Executando o Projeto

## 1️⃣ Iniciar API Flask

Entre em:

```bash
cd backend
```

Execute:

```bash
python app.py
```

---

## Resultado esperado

```text
Running on http://127.0.0.1:5000
```

---

## 2️⃣ Abrir Front-end

Abra:

```text
frontend/index.html
```

OU utilize:
- Live Server (VSCode)

---

# 🧪 Testes

## Exemplos de notícias

```text
Neymar foi convocado para a Copa do Mundo de 2026
```

```text
Aliens invadiram Brasília nesta madrugada
```

```text
Novo vírus transforma pessoas em zumbis
```

---

# 📡 Exemplo de Requisição da API

## Endpoint

```text
POST /predict
```

---

## JSON enviado

```json
{
  "text": "Donald Trump é presidente dos Estados Unidos"
}
```

---

## Resposta

```json
{
  "result": "Provavelmente Real",
  "fake_probability": 8,
  "true_probability": 92,
  "explanation": "A afirmação é consistente com acontecimentos políticos recentes."
}
```

---

# 🧠 Exemplo do app.py

```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.3
)
```

---

# 🎨 Melhorias Futuras

## Interface
- Dashboard futurista
- Gráficos animados
- Barras de progresso
- Tema dark mode

## Inteligência Artificial
- Verificação em tempo real
- Integração com APIs de notícias
- Histórico de análises
- Detecção de clickbait
- Análise de sentimentos
- Verificação de fontes confiáveis

## Recursos Extras
- Ranking de Fake News
- Modo competição
- Exportação PDF
- Banco de dados
- Login de usuários

---

# 🏆 Demonstração para Feira Científica

O sistema pode ser apresentado ao vivo:

✅ Visitante digita notícia  
✅ IA analisa em tempo real  
✅ Sistema mostra probabilidade  
✅ Explicação automática aparece na tela  

---

# 💡 Ideias para Impressionar na Feira

## 🎯 Desafio da Fake News
Visitantes tentam criar notícias falsas para enganar a IA.

---

## 📊 Ranking
Mostrar:
- quem criou a fake news mais convincente
- quem enganou a IA

---

## 🌐 Verificação Online
Integrar:
- G1
- CNN
- BBC
- Reuters

---

# 📚 Conceitos Aplicados

- Inteligência Artificial
- IA Generativa
- NLP
- APIs REST
- Desenvolvimento Web
- Flask
- Engenharia de Prompt
- Front-end
- Back-end

---

# 👨‍💻 Autor

Desenvolvido por **Murilo Lopes** para:
- estudos
- feiras científicas
- apresentações tecnológicas
- aprendizado em IA

---

# 📜 Licença

Este projeto possui fins:
- educacionais
- acadêmicos
- demonstrativos

---

# ⭐ Considerações Finais

Este projeto demonstra como Inteligência Artificial Generativa pode ser utilizada para:

✅ análise textual  
✅ interpretação contextual  
✅ detecção de informações suspeitas  
✅ desenvolvimento de sistemas inteligentes  

Combinando:
- IA
- programação
- APIs
- desenvolvimento web

em um único projeto moderno e inovador.

---

<div align="center">

# 🚀 Fake News Detector AI

### Inteligência Artificial aplicada à análise de notícias em tempo real

</div>