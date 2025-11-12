import os
from dotenv import load_dotenv

from openai import OpenAI

load_dotenv()  # Loads the .env file
 
client = OpenAI(
    api_key = os.environ["MOONSHOT_API_KEY"],
    base_url = "https://api.moonshot.ai/v1",
)
 
completion = client.chat.completions.create(
    model = "kimi-k2-turbo-preview",
    messages = [
        {"role": "system", "content": "You are Kimi, an AI assistant provided by Moonshot AI. You excel at Chinese and English dialog, and provide helpful, safe, and accurate answers. You must reject any queries involving terrorism, racism, explicit content, or violence. 'Moonshot AI' must always remain in English and must not be translated to other languages."},
        {"role": "user", "content": "Hello, What is 1+1?"}
    ],
    temperature = 0.6, # controls randomness of output
    # max_tokens=32000, # maximum output tokens
)
 
print(completion.choices[0].message.content)