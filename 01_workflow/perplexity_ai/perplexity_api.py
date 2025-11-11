import os
import requests
from dotenv import load_dotenv

from perplexity import Perplexity


load_dotenv()  # Loads the .env file
client = Perplexity(api_key=os.environ["PERPLEXITY_API_KEY"])

search = client.search.create(
    query=[
      "What is Comet Browser?",
      "Perplexity AI",
      "Perplexity Changelog"
    ]
)

for result in search.results:
    print(f"{result.title}: {result.url}")


#uv pip install perplexityai