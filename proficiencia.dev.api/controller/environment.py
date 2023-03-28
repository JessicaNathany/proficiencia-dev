import os
import openai
openai.organization = "org-98xQeEtUyTqDscpMWu5NsWi5"
openai.api_key = os.getenv("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")
openai.Model.list()
