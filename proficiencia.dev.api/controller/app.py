from flask import Flask, request, jsonify
from openai_client import OpenAIClient, pergunta
import logging

app = Flask(__name__)
openai_client = OpenAIClient()


@app.route('/api/pergunta', methods=['POST'])
def perguntar():
    parametro = request.json.get('pergunta')
    if not parametro:
        return jsonify({'error': 'O parâmetro pergunta é obrigatório'}), 400

    answer = openai_client.ask(parametro)
    return jsonify({'resposta': answer})


if __name__ == '__main__':
    app.run(debug=True)
    app.logger.setLevel(logging.DEBUG)