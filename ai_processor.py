import ollama
from scrap import Scrap
import json

class IA():
    def __init__(self):
        self.prompt = None

    def analyze_with_ai(self, raw_data):
        self.prompt = f"""
        Your task is to convert raw data into a structured JSON.
        RULES:
        1. Return ONLY the JSON. No explanations or Markdown formatting.
        2. If status is 'Success', the format MUST be: {{"Status": "Success", "Price": "value"}}
        3. If status is 'Failure', the format MUST be: {{"Status": "Failure", "Price": "None"}}

        Data to process: {raw_data}
        """
        response = ollama.chat(model='gemma3:4b', messages=[
            {
                'role': 'user',
                'content': self.prompt,
            },
        ])
        
        return response['message']['content']

    def format_response(self, response):
        cleaned = response.replace("```json", "").replace("```", "").strip()
        data_dict = json.loads(cleaned)
        return data_dict
    

