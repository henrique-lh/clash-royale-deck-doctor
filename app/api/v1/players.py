from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.infrastructure.database.session import get_db
from app.infrastructure.external.clash_royale.clash_api_settings import get_clash_api_settings, ClashAPISettings
from app.infrastructure.external.ollama.ollama_client import OllamaClient
from app.infrastructure.external.ollama.ollama_settings import OllamaSettings, get_ollama_settings
from app.infrastructure.repository.sql_battle_repository import SQLBattleRepository
from app.infrastructure.external.clash_royale.clash_api_client import ClashAPIClient
from app.schemas.analysis_schema import AnalysisResponse
from app.schemas.refresh_schema import RefreshResponse
from app.use_cases.analyze_player import AnalyzePlayerUseCase
from app.use_cases.refresh_player import RefreshPlayerUseCase


router = APIRouter()


@router.post("/players/{tag}/refresh", response_model=RefreshResponse)
def refresh_player(
        tag: str, db: Session = Depends(get_db),
        clash_api_settings: ClashAPISettings = Depends(get_clash_api_settings),
):

    repository = SQLBattleRepository(db)
    clash_api_client = ClashAPIClient(api_key=clash_api_settings.api_key)

    use_case = RefreshPlayerUseCase(repository, clash_api_client)

    return use_case.execute(tag)


@router.get("/players/{tag}/analysis", response_model=AnalysisResponse)
def analyze_player(
        tag: str,
        db: Session = Depends(get_db),
        ollama_settings: OllamaSettings = Depends(get_ollama_settings),
):

    repository = SQLBattleRepository(db)
    use_case = AnalyzePlayerUseCase(repository)
    ollama_client = OllamaClient(ollama_settings.api_key)

    return use_case.execute(tag, ollama_client)
