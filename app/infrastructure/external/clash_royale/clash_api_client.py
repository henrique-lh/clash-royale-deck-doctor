import httpx


class ClashAPIClient:

    BASE_URL = "https://api.clashroyale.com/v1"

    def __init__(self, api_key: str):
        self.headers = {
            "Authorization": f"Bearer {api_key}"
        }

    @staticmethod
    def __encode_tag(tag: str):
        return tag.replace("#", "%23")

    async def get_battle_log(self, player_tag: str):
        tag = self.__encode_tag(player_tag)
        url = f"{self.BASE_URL}/players/{tag}/battlelog"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    async def get_current_deck(self, player_tag: str):
        tag = self.__encode_tag(player_tag)
        url = f"{self.BASE_URL}/players/{tag}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
