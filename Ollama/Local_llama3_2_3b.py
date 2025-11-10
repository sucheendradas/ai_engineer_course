import os
import requests
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

OLLAMA_BASE = os.getenv("OLLAMA_API_BASE", "http://localhost:11434")
MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b")

prompt = "write jump code for unity engine"

print(f"\n🧠 Using model: {MODEL}\n")
print(f"💬 Prompt: {prompt}\n")
print("🤖 Ollama response:\n")

# Send prompt to Ollama
payload = {
    "model": MODEL,
    "prompt": prompt,
}

response = requests.post(f"{OLLAMA_BASE}/api/generate", json=payload, stream=True)

# Stream and parse the output line by line
for line in response.iter_lines():
    if not line:
        continue
    try:
        data = json.loads(line.decode("utf-8"))
        if "response" in data:
            print(data["response"], end="", flush=True)
    except json.JSONDecodeError:
        continue

print("\n\n✅ Done.")
