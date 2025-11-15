
import os
import dotenv
dotenv.load_dotenv()

from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = os.getenv("NVIDIA_API_KEY")
)

model_1 = "qwen/qwen2.5-coder-32b-instruct"
model_2 = "deepseek-ai/deepseek-r1"
model_4 = "meta/llama-3.3-70b-instruct"
model_5 = "openai/gpt-oss-20b"         

completion = client.chat.completions.create(
  model=model_2,
  messages=[{"role":"user","content":"what is sun"}],
  temperature=0.2,
  top_p=0.7,
  max_tokens=1024,
  stream=False
)


# normal output
print(completion.choices[0].message)

