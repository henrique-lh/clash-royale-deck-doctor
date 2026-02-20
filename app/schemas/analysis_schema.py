from typing import List
from pydantic import BaseModel, Field


class PlayerStats(BaseModel):
    total_battles: int = Field(..., examples=[25])
    wins: int = Field(..., examples=[14])
    losses: int = Field(..., examples=[11])
    winrate: float = Field(..., examples=[56.0])
    avg_elixir: float = Field(..., examples=[3.4])
    avg_elixir_leaked: float = Field(..., examples=[9.8])


class MatchupEntry(BaseModel):
    card: str = Field(..., examples=["Inferno Tower"])
    appearances: int = Field(..., examples=[5])


class Diagnosis(BaseModel):
    deck_type: str = Field(..., examples=["Control"])
    problems: List[str] = Field(default_factory=list)
    recommendations: List[str] = Field(default_factory=list)


class AnalysisResponse(BaseModel):
    stats: PlayerStats
    matchups: List[MatchupEntry]
    diagnosis: Diagnosis
