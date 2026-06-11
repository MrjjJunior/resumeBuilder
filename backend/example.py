
from openai import OpenAI
import os
import sys

client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

prompt = sys.argv[1]

response = client.responses.create(
    input=prompt,
    model="openai/gpt-oss-20b",
)
print(response.output_text)

