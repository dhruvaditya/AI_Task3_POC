import  requests
from transformers import pipeline
text_generator=pipeline("text_generation",model="google/bard-large-cnn")
prompt=("Enhance the text: Loan Pending with a bank")
generated_text=text_generator(prompt,max_lenth=50, num_return_sequence=3)
prompt = "Generate a product description for a flying skateboard."
headers = {"Authorization": f"Bearer {API_KEY}"} if API_KEY else {}
response = requests.post("https://api.openai.com/v1/chat/completions",
                         headers=headers,
                         json={"model": "gpt-4.0-turbo", "messages": [{"role": "system", "content": prompt}]})
generated_text = response.json()["choices"][0]["message"]["content"]
print(generated_text)
