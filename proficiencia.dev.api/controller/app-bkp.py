from flask import Flask, request, jsonify
from clientgpt import ClientGpt, pergunta
#import clientgpt
import logging

app = Flask(__name__)
clientgpt = ClientGpt()

#ClientGpt = clientgpt.ClientGpt()

@app.route('/api/pergunta', methods=['POST'])
def perguntar():
    parametro = request.json.get('pergunta')
    if not parametro:
        return jsonify({'error': 'O parâmetro pergunta é obrigatório'}), 400

    answer = ClientGpt.ask(parametro)
    return jsonify({'resposta': answer})


if __name__ == '__main__':
    app.run(debug=True)
    app.logger.setLevel(logging.DEBUG)