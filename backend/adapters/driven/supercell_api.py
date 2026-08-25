import os
import httpx
from fastapi import HTTPException
from ports.driven import BrawlStarsClientPort
from core.models import PlayerDomain

class SupercellApiAdapter(BrawlStarsClientPort):
    def __init__(self):
        self.base_url = "https://api.brawlstars.com/v1"
        self.token = os.getenv("BRAWL_STARS_TOKEN") or os.getenv("BRAWL_API_KEY", "")
        self.proxy_url = os.getenv("FIXIE_URL") or os.getenv("HTTPS_PROXY") or os.getenv("HTTP_PROXY")

    async def fetch_player_by_tag(self, tag: str) -> PlayerDomain:
        url = f"{self.base_url}/players/%23{tag}"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json"
        }

        client_kwargs = {"proxy": self.proxy_url} if self.proxy_url else {}

        async with httpx.AsyncClient(**client_kwargs) as client:
            try:
                print(f"Fetching player data for tag: {tag} from Supercell API...")
                response = await client.get(url, headers=headers, timeout=10.0)
                
                if response.status_code == 404:
                    raise HTTPException(status_code=404, detail="Player tag not found.")
                elif response.status_code == 403:
                    raise HTTPException(status_code=403, detail="Authentication failed with Supercell API. Verify token or Whitelisted IP.")
                
                response.raise_for_status()
                raw_data = response.json()
                
                return PlayerDomain(**raw_data)
                
            except httpx.RequestError as exc:
                raise HTTPException(status_code=500, detail=f"Failed to communicate with external Supercell API: {exc}")
