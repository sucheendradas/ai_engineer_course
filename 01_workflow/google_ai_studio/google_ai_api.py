import os
from dotenv import load_dotenv
from google import genai


load_dotenv()  # Loads the .env file
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key = os.environ["GEMINI_API_KEY"])

#client = genai.Client(api_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="2+2=?"
)
print(response.text)

#https://ai.google.dev/gemini-api/docs/quickstart
# in your venu --> uv pip install google-genai
