from pydantic import BaseModel, Field
from typing import List, Optional

# --- SUB-MODELS ---
class ClubInfo(BaseModel):
    tag: str
    name: str

class SkinInfo(BaseModel):
    id: int
    name: str

class ItemInfo(BaseModel):
    """Generic model for Gadgets, Star Powers, and Hypercharges"""
    id: int
    name: str

class GearInfo(BaseModel):
    id: int
    name: str
    level: int

class BrawlerBuffies(BaseModel):
    gadget: bool
    star_power: bool = Field(alias="starPower")
    hyper_charge: bool = Field(alias="hyperCharge")

    class Config:
        populate_by_name = True


# --- THE CORE BRAWLER MODEL ---
class BrawlerDomain(BaseModel):
    id: int
    name: str
    power: int
    rank: int
    trophies: int
    highest_trophies: int = Field(alias="highestTrophies")
    prestige_level: int = Field(alias="prestigeLevel")
    current_win_streak: int = Field(alias="currentWinStreak")
    max_win_streak: int = Field(alias="maxWinStreak")
    
    skin: Optional[SkinInfo] = None
    gadgets: List[ItemInfo] = []
    star_powers: List[ItemInfo] = Field(default=[], alias="starPowers")
    hyper_charges: List[ItemInfo] = Field(default=[], alias="hyperCharges")
    gears: List[GearInfo] = []
    buffies: Optional[BrawlerBuffies] = None

    class Config:
        populate_by_name = True


# --- THE MAIN PLAYER DOMAIN MODEL ---
class PlayerDomain(BaseModel):
    tag: str
    name: str
    name_color: str = Field(alias="nameColor")
    trophies: int
    highest_trophies: int = Field(alias="highestTrophies")
    exp_level: int = Field(alias="expLevel")
    
    # Game Mode Statistics
    victories_3vs3: int = Field(alias="3vs3Victories")
    solo_victories: int = Field(alias="soloVictories")
    duo_victories: int = Field(alias="duoVictories")
    
    # Ranked / Competitive Season Stats
    ranked_rank: Optional[int] = Field(None, alias="rankedRank")
    ranked_rank_name: Optional[str] = Field(None, alias="rankedRankName")
    ranked_elo: Optional[int] = Field(None, alias="rankedElo")
    
    # Social / Infrastructure
    club: Optional[ClubInfo] = None
    brawlers: List[BrawlerDomain] = []

    class Config:
        populate_by_name = True

    # --- DOMAIN BUSINESS LOGIC ---
    def get_brawler_count(self) -> int:
        return len(self.brawlers)

    def get_max_level_brawlers_count(self) -> int:
        """Counts brawlers at power level 11"""
        return sum(1 for b in self.brawlers if b.power == 11)

    def get_hypercharged_brawlers_count(self) -> int:
        """Counts how many brawlers have an unlocked hypercharge item"""
        return sum(1 for b in self.brawlers if len(b.hyper_charges) > 0)

class MetricComparison(BaseModel):
    current: int
    total_needed_for_max: int
    leftover_needed: int
    percentage_completed: float

class ProgressionMetrics(BaseModel):
    # Total Gold to max absolutely everything
    gold_max: MetricComparison

    # Total PP to max absolutely everything
    pp_max: MetricComparison

    # Gold and left to push all brawlers to Power 11 (excluding items)
    gold_power_11_only: MetricComparison
    
    # PP and left to push all brawlers to Power 11 (excluding items)
    pp_power_11_only: MetricComparison

    # Gold needed to unlock ALL existing gears across all brawlers
    gears_completion: MetricComparison
    
    # Gold needed to unlock all buffies
    buffies_gold: MetricComparison
    
    # PP needed to unlock all buffies
    buffies_pp: MetricComparison

    # Gold needed to buy all existing Hypercharges
    hypercharges_completion: MetricComparison