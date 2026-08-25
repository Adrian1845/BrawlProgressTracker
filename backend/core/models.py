from pydantic import BaseModel, Field, field_validator
from typing import List, Optional

# --- SUB-MODELS ---
class ClubInfo(BaseModel):
    tag: str
    name: str

class ProfileIconInfo(BaseModel):
    id: int

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
    icon: Optional[ProfileIconInfo] = None
    brawlers: List[BrawlerDomain] = []

    class Config:
        populate_by_name = True

    @field_validator("club", mode="before")
    @classmethod
    def empty_club_becomes_none(cls, value):
        if value in ({}, None, ""):
            return None
        return value

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

class ProgressMetricGroup(BaseModel):
    count: Optional[MetricComparison] = None
    gold: Optional[MetricComparison] = None
    pp: Optional[MetricComparison] = None

class ProgressionMetricsV2(BaseModel):
    # Total gold and PP to max all brawlers and owned progression systems
    max_level: ProgressMetricGroup

    # How many brawlers are at Power 11 and their resource progress
    power_11: ProgressMetricGroup

    # How many gadgets are owned and the gold needed to unlock the rest
    gadgets: ProgressMetricGroup

    # How many star powers are owned and the gold needed to unlock the rest
    star_powers: ProgressMetricGroup

    # How many gears are owned and the gold needed to unlock the rest
    gears: ProgressMetricGroup

    # How many buffies are owned and the gold/PP needed to unlock the rest
    buffies: ProgressMetricGroup

    # How many hypercharges are owned and the gold needed to unlock the rest
    hypercharges: ProgressMetricGroup
