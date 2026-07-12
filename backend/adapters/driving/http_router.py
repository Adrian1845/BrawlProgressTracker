 
from fastapi import APIRouter, Depends
from backend.adapters.driven.supercell_api import SupercellApiAdapter
from backend.ports.driven import BrawlStarsClientPort
from backend.core.services import TrackerAnalyticService
from backend.core.models import PlayerDomain, ProgressionMetrics
from pydantic import BaseModel

router = APIRouter(prefix="/api/player", tags=["Player Metrics"])

# Simple dependency injector utility to resolve the port to our specific adapter instance instance
def get_brawl_stars_client() -> BrawlStarsClientPort:
    return SupercellApiAdapter()

# Schema for the aggregated payload sent to our frontend client
class PlayerProfileReportResponse(BaseModel):
    profile: PlayerDomain
    metrics: ProgressionMetrics

@router.get("/{player_tag}", response_model=PlayerProfileReportResponse)
async def get_player_progression_report(
    player_tag: str, 
    client: BrawlStarsClientPort = Depends(get_brawl_stars_client)
):
    # 1. Clean the tag string to prevent URL corruption issues
    clean_tag = player_tag.strip().replace("#", "").replace("%23", "")
    
    # 2. Invoke the driven client adapter to securely pull down model-mapped data
    player_domain = await client.fetch_player_by_tag(clean_tag)
    
    # 3. Process the rich domain data model using the pure math core analytic service
    progression_metrics = TrackerAnalyticService.calculate_progression_metrics(player_domain)
    
    # 4. Return the beautifully compiled response object
    return PlayerProfileReportResponse(
        profile=player_domain,
        metrics=progression_metrics
    )