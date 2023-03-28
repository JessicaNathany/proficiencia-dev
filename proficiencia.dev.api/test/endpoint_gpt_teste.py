from flask import Flask
app = Flask(__name__)
app.run(debug=True)
import openai_secret_manager
import requests
import openai
import os

API_ENDPOINT = "https://api.openai.com/v1/models"
API_KEY = "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"
OPENAI_MODEL = "davinci" 
OPENAI_ORGANIZATION = "org-98xQeEtUyTqDscpMWu5NsWi5" 

# Definir rota para o endpoint GET da OpenAI API
@app.route("/api/openai")

def openai_api_get():
    
    pergunta = 'Qual é a capital do Brasil?'
    completions = openai.Completion.create(
        engine="davinci",
        prompt=f"Responda a seguinte pergunta:\n{pergunta}\nResposta:",
        max_tokens=1024,
    )
    resposta = completions.choices[0].text.strip()

    return {"resposta": resposta}

if __name__ == "__main__":
    app.run()