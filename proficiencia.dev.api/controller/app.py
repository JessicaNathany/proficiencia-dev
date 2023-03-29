# Flask é um framework para criar aplicações web com Python
# 1. objetivo - criar uma api que faça uam consulta no endpoint do openai, fazendo uma pergunta e obtendo resposta ao chatgpt
# 2. url base - localhost.com 
# 3. endpoints 
#   - localhost/app/pergunta (POST)
# 4. quais recursos - POST (para fazer uma pergunta ao chatgpt)

# importando biblioteca do Flask
from flask import Flask, jsonify, request

app = Flask(__name__)

pergunta =  {'Quais são as linguagens de programação mais usadas no backend?'}

# faz a pergunta ao chatgpt
@app.route('/api/pergunta', methods=['POST'])
def perguntar(pergunta):
    url = 'https://api.openai.com/v1/completions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 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',
    }

    data = {
        'prompt': pergunta,
        'max_tokens': 7,
        'temperature': 0,
        'model' : 'text-davinci-003',
        'stream': False,
        'logprobs': None,
        'stop': '\n'
    }

    response = request.post(url, headers=headers, json=data)
    return response.json()
    
    
app.run(port=5000, host='localhost', debug=True)