import os
import json
from groq import Groq
import ollama

class IA():
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if self.api_key:
            self.client = Groq(api_key=self.api_key)
        else:
            self.ollama = ollama

    def analyze_with_ai(self, raw_data):
        prompt = f"""
        Your task is to convert raw data into a structured JSON.
        RULES:
        1. Return ONLY the JSON. No explanations or Markdown formatting.
        2. Format: {{"Status": "Success", "Price": "value"}}
        3. If failure: {{"Status": "Failure", "Price": "None"}}

        Data: {raw_data}
        """
        
        if self.api_key:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )
            return completion.choices[0].message.content
        else:
            response = self.ollama.chat(model='gemma3:4b', messages=[
                {'role': 'user', 'content': prompt},
            ])
            return response['message']['content']

    def format_response(self, response):
        try:
            cleaned = response.replace("```json", "").replace("```", "").strip()
            return json.loads(cleaned)
        except:
            return {"Status": "Failure", "Price": "None"}
