import requests

def test_chat_gpt():
    url = 'http://localhost:5000/chatgpt'
    payload = {'question': 'Quais as linguagens de programação existente?'}
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert 'answer' in response.json()
    assert f'Status code: {response.status_code}'
 