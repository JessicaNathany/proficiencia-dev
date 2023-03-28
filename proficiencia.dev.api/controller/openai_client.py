import openai
import config
import requests


class OpenAIClient:
    def __init__(self):
        openai.api_key = config.API_KEY
        openai.api_endpoint = config.OPENAI_ENDPOINT

    def ask(self, question):
        prompt = f"{question}\n"
        response = openai.Completion.create(
            prompt="Crie um simulado de Python para processo seletivo",
            model=config.OPENAI_MODEL,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )

        return response.choices[0].text.strip()


def perguntar(parametro_pergunta):
    query_params = {
        'model': config.OPENAI_MODEL,
        'prompt': parametro_pergunta,
    }
    resposta = requests.post(
        'https://api.openai.com/v1/completions',
        json=query_params,
        headers={
            'Authorization': f'Bearer {config.API_KEY}',
            'Content-Type': 'application/json'
        },
    )

    completions = resposta.json()['choices'][0]['text']
    return completions

