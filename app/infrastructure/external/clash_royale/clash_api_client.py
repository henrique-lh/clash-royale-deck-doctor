import requests


class ClashAPIClient:

    BASE_URL = "https://api.clashroyale.com/v1"

    def __init__(self, api_key: str):
        self.headers = {
            "Authorization": f"Bearer {api_key}"
        }

    def get_battle_log(self, player_tag: str):
        tag = player_tag.replace("#", "%23")
        url = f"{self.BASE_URL}/players/{tag}/battlelog"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
