from pydantic import BaseModel


class RefreshResponse(BaseModel):
    player_tag: str
    battles_imported: int
