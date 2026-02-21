import httpx

class OllamaClient:

    API_URL = "https://router.huggingface.co/v1/chat/completions"
    MODEL = "meta-llama/Llama-3.3-70B-Instruct"

    def __init__(self, api_key: str):
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    async def generate_recommendation(self, problems: list[str], current_deck: list[dict]) -> list[str]:
        prompt = f"""You are now a professional Clash Royale player, able to offer potential solutions to the following issues.

## Task
given a list of problems, and the current user deck, write a recommendation for how to solve them. You must follow the rules below.
use all inputs to think about possible solutions.

## Input
problems with the deck: {problems}
current user clash royale deck: {current_deck}

## Rules
- you must write a recommendation for how to solve the problems
- the recommendation should be a single sentence, brief and concise
- if necessary, it can be split into multiple sentences
- you must give at least one solution for each problem
- you must write the answer in portuguese
- you must separate the solutions with a semicolon, one after the other
- list possible counters for the cards that the user has the most difficulty with
"""
        payload = {
            "model": self.MODEL,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 500,
            "temperature": 0.3
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(self.API_URL, headers=self.headers, json=payload)
        if response.status_code != 200:
            raise Exception(f"Error generating recommendation: {response.text}")
        result = response.json()
        clean_response = result["choices"][0]["message"]["content"].strip()
        return clean_response.split(";") or ["No explanation available."]
