import os
import json
import re
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class IA():
    def __init__(self):

        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def analyze_with_ai(self, raw_data1: str, raw_data2: str) -> tuple[bool, str, str]:
        try:
            prompt = f"""
            Extract the CURRENT CASH PRICE for TWO items from the HTML provided.
            
            RULES:
            1. Return a JSON LIST with exactly 2 objects.
            2. For each price: Extract only digits. If there are cents, IGNORE them.
            Example: R$ 22.599,99 -> "22599" (NO cents).
            3. Format: [
                {{"item": RTX5090, "Status": "Success", "Price": "xxxxx"}},
                {{"item": RTX4090, "Status": "Success", "Price": "xxxxx"}}
            ]

            Data 1: {raw_data1}
            Data 2: {raw_data2}
            """
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"} 
            )
            return True, "Analyzed successfully.", completion.choices[0].message.content
        except Exception as e:
            return False, f"Error: {e}", ""
    def format_response(self, response: str) -> dict:
        try:
            match = re.search(r'[\{\[].*[\}\]]', response, re.DOTALL)
            if match:
                cleaned = match.group(0)
                data = json.loads(cleaned)
                if isinstance(data, dict) and "items" in data:
                    data = data["items"]

                return True, "success", data
            else:
                raise ValueError("no json found")
                
        except Exception as e:
            return False, f"Fail: {str(e)}", {"Price": "0"}
