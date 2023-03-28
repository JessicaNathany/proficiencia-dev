import requests
from environment import api_key

def perguntar_chatgpt(pergunta):
    url = 'https://api.openai.com/v1/engines/davinci-codex/completions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    data = {
        'prompt': pergunta,
        'max_tokens': 50,
        'temperature': 0.5
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        raise ValueError('Request ao ChatGPT falhou.')

    return response.json()