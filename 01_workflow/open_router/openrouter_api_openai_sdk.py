import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Loads the .env file

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key= os.environ["OPENROUTER_API_KEY"],
)

# Use the standard chat completions endpoint
response = client.chat.completions.create(
    #model="openai/gpt-4o",  # Using a standard mini model name
    #model="openai/gpt-4o",  # Using a standard mini model name
    model="kwaipilot/kat-coder-pro:free",
    messages=[
        {"role": "user", "content": "what is bitcoin?"}
    ],
    max_tokens=1000
)

# Access the content from the response object
print(response.choices[0].message.content)