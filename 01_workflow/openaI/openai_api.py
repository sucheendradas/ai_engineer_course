# no free quota for deveeopesrs account
#https://platform.openai.com/docs/quickstart
# uv pip install openai

import os
from dotenv import load_dotenv
load_dotenv()  # Loads the .env file
from openai import OpenAI
client = OpenAI(api_key=os.environ["OPENAI_API_KEY_ZOHO"])

#o3-mini
#gpt-4.1-nano

response = client.responses.create(
    model="gpt-4.1-nano",
    input="2+2=?"
)

print(response.output_text)
