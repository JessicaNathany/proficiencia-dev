import os
import openai

openai.organization = "org-98xQeEtUyTqDscpMWu5NsWi5"
openai.api_key = os.getenv("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")
openai.Model.list()