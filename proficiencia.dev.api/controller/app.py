from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# faz a pergunta ao chatgpt
@app.route('/api/pergunta', methods=['POST'])
def pergunta():
    obem_pergunta = request.get_json()
    pergunta = obem_pergunta['pergunta']
    url = 'https://api.openai.com/v1/completions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer API-KEY',
    }

    data = {
        'prompt': pergunta,
        'max_tokens': 3000,
        'model' : 'text-davinci-003',
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()

    
if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)