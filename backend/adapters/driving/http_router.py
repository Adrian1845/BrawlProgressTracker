 
from fastapi import APIRouter, Depends
from adapters.driven.supercell_api import SupercellApiAdapter
from ports.driven import BrawlStarsClientPort
from core.services import TrackerAnalyticService
from core.models import PlayerDomain, ProgressionMetrics
from pydantic import BaseModel

router = APIRouter(prefix="/api/player", tags=["Player Metrics"])

def get_brawl_stars_client() -> BrawlStarsClientPort:
    return SupercellApiAdapter()

class PlayerProfileReportResponse(BaseModel):
    profile: PlayerDomain
    metrics: ProgressionMetrics

@router.get("/{player_tag}", response_model=PlayerProfileReportResponse)
async def get_player_progression_report(
    player_tag: str, 
    client: BrawlStarsClientPort = Depends(get_brawl_stars_client)
):
    clean_tag = player_tag.strip().replace("#", "").replace("%23", "")
    
    player_domain = await client.fetch_player_by_tag(clean_tag)
    
    progression_metrics = TrackerAnalyticService.calculate_progression_metrics(player_domain)
    
    return PlayerProfileReportResponse(
        profile=player_domain,
        metrics=progression_metrics
    )