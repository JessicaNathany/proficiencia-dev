import os
import requests
import openai

openai.organization = "org-98xQeEtUyTqDscpMWu5NsWi5"

api_key = os.environ.get('OPENAI_API_KEY')
headers = {'Authorization': f'Bearer {api_key}'}