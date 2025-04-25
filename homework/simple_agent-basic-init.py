import os
from dotenv import load_dotenv

from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")


llm_name = "gpt-4o-mini"

client = OpenAI(api_key=openai_key)

response = client.chat.completions.create(
    model=llm_name,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "넬슨 만델라는 누구?"},
    ],
)
print(response.choices[0].message.content)

# Create ou