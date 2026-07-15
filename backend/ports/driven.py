from abc import ABC, abstractmethod
from core.models import PlayerDomain

class BrawlStarsClientPort(ABC):
    
    @abstractmethod
    async def fetch_player_by_tag(self, tag: str) -> PlayerDomain:
        """Fetch raw player profile from an external data source and map it to the domain layer."""
        pass