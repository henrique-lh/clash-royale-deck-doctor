from fastapi import APIRouter, Depends

from app.infrastructure.cache.redis_client import RedisClient
from app.infrastructure.external.clash_royale.clash_api_settings import (
    get_clash_api_settings,
    ClashAPISettings,
)
from app.infrastructure.external.ollama.ollama_client import OllamaClient
from app.infrastructure.external.ollama.ollama_settings import (
    OllamaSettings,
    get_ollama_settings,
)
from app.infrastructure.repository.redis_battle_repository import RedisBattleRepository
from app.infrastructure.external.clash_royale.clash_api_client import ClashAPIClient
from app.schemas.analysis_schema import AnalysisResponse
from app.schemas.refresh_schema import RefreshResponse
from app.use_cases.analyze_player import AnalyzePlayerUseCase
from app.use_cases.refresh_player import RefreshPlayerUseCase


router = APIRouter()


@router.post("/players/{tag}/refresh", response_model=RefreshResponse)
async def refresh_player(
    tag: str,
    clash_api_settings: ClashAPISettings = Depends(get_clash_api_settings),
):

    redis_client = RedisClient()
    repository = RedisBattleRepository(redis_client)

    clash_api_client = ClashAPIClient(api_key=clash_api_settings.api_key)

    use_case = RefreshPlayerUseCase(repository, clash_api_client)

    return await use_case.execute(tag)


@router.get("/players/{tag}/analysis", response_model=AnalysisResponse)
async def analyze_player(
    tag: str,
    ollama_settings: OllamaSettings = Depends(get_ollama_settings),
    clash_api_settings: ClashAPISettings = Depends(get_clash_api_settings),
):

    redis_client = RedisClient()
    repository = RedisBattleRepository(redis_client)

    use_case = AnalyzePlayerUseCase(repository)
    ollama_client = OllamaClient(ollama_settings.api_key)

    clash_api_client = ClashAPIClient(api_key=clash_api_settings.api_key)

    return await use_case.execute(tag, ollama_client, clash_api_client)
