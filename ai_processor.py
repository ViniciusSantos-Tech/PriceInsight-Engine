import os
import json
from dotenv import load_dotenv
from groq import Groq
load_dotenv()

class IA():
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def analyze_with_ai(self, raw_data: str) -> tuple[bool, str, str]:
        try:
            prompt = f"""
            Your task is to extract the CURRENT CASH PRICE (PIX/Boleto) from the provided HTML data and convert it into a structured JSON.

            STRICT RULES:
            1. Return ONLY the raw JSON. No markdown blocks (```json), no explanations, no conversational text.
            2. Extract ONLY the single lowest cash price available. Ignore installment prices (parcelas) or total credit prices.
            3. Format: {{"Status": "Success", "Price": "xx.xxx"}}
            4. Numeric Format: Use ONLY plain digits. NO periods (.), NO commas (,). If the price is 29.909,00, return "29909".
            - Correct: "xxxxx"
            - Incorrect: "xx.xxx,xx" or "R$ xx.xxx,xx"
            5. If the price cannot be clearly found, return: {{"Status": "Failure", "Price": "None"}}


            Data: {raw_data}
            """
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )
            return True, "Analyzed successfully.", completion.choices[0].message.content
        except Exception as e:
            return False, f"Error: {e}", ""
    
    def format_response(self, response: str) -> dict:
        try:
            cleaned = response.replace("```json", "").replace("```", "").strip()
            data = json.loads(cleaned)
            if isinstance(data, list):
                data = data[:5]
            return True, "sucess", data
        except Exception as e:
            return False, f"Error: {str(e)}", {"Price": "0"}
