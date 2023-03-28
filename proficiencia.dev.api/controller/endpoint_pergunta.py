from flask import Flask, request
from flask_restful import Resource, Api
import requests
from environment import api_key

class ChatGPT(Resource):
    def post(self):
        question = request.json['question']
        headers = {'Authorization': f'Bearer {api_key}'}
        payload = {'question': question}
        response = requests.post('https://api.openai.com/v1/answers', json=payload, headers=headers)
        answer = response.json()['answers'][0]['text']
        return {'answer': answer}
    
        

app = Flask(__name__)
api = Api(app)
api.add_resource(ChatGPT, '/chatgpt')

    

if __name__ == '__main__':
    app.run(debug=True)