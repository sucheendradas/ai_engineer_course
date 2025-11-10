import os
from dotenv import load_dotenv
from ollama import Client

# Load .env file
load_dotenv()

# Get key safely
api_key = os.getenv("OLLAMA_API_KEY")

if not api_key:
    raise ValueError("⚠️ OLLAMA_API_KEY not found. Check your .env file path or variable name.")

# Initialize client
client = Client(
    host="https://ollama.com",
    headers={'Authorization': f'Bearer {api_key}'}
)

messages = [
  {'role': 'user', 'content': 'find best stock in india?'}
]

# Stream chat output
for part in client.chat('gpt-oss:120b', messages=messages, stream=True):
    print(part['message']['content'], end='', flush=True)

#https://ollama.com/library/gpt-oss