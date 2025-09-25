from openai import OpenAI
from OpenAIProductKey import readKeyFromFile

key = readKeyFromFile("key.txt")

print(key)
"""
client = OpenAI(
  api_key=key
)

response = client.responses.create(
  model="gpt-5-nano",
  input="write a haiku about ai",
  store=True
)

print(response.output_text)
"""
