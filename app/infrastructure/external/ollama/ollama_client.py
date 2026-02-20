import requests


class OllamaClient:

    API_URL = "https://router.huggingface.co/v1/chat/completions"
    MODEL = "meta-llama/Llama-3.3-70B-Instruct"

    def __init__(self, api_key: str):
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def generate_recommendation(self, problems: list[str]) -> list[str]:
        prompt = f"""You are now a professional Clash Royale player, able to offer potential solutions to the following issues.

## Task
Given a list of problems, write a recommendation for how to solve them.

## Input
Problems: {problems}

## Rules
- You must write a recommendation for how to solve the problems. The recommendation should be a single sentence, brief and concise. If necessary, it can be split into multiple sentences.
- You must give at least one solution for each problem.
- You must not use any external resources.
- You must write the answer in portuguese.
- You must not use any emojis.
- You must not use any special characters.
- You must not use any markdown.
- You must not use any code.
- You must separate the solutions with a semicolon, one after the other.
"""
        payload = {
            "model": self.MODEL,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 500,
            "temperature": 0.3
        }

        response = requests.post(self.API_URL, headers=self.headers, json=payload)
        if response.status_code != 200:
            raise Exception(f"Error generating recommendation: {response.text}")
        result = response.json()
        clean_response = result["choices"][0]["message"]["content"].strip()
        return clean_response.split(";") or ["No explanation available."]
