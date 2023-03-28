from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)

API_KEY = "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"
OPENAI_MODEL = "davinci" 
OPENAI_ENDPOINT = 'https://api.openai.com/v1/completions'
OPENAI_ORGANIZATION = "org-98xQeEtUyTqDscpMWu5NsWi5" 




@app.route('/api/perguntagpt', methods=['POST'])
def funcao1():
    pergunta = {
    'pergunta': 'Qual é a capital do Brasil?'
}
    perguntar_chatgpt(pergunta)
    


def perguntar_chatgpt(pergunta):
    url = 'https://api.openai.com/v1/engines/davinci-codex/completions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}',
    }

    data = {
        'prompt': pergunta,
        'max_tokens': 50,
        'temperature': 0.5,
        "model" : OPENAI_MODEL
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        raise ValueError('Request ao ChatGPT falhou.')

    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
    
    app.logger.setLevel(logging.DEBUG)