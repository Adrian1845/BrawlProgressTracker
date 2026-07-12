from backend.core.constants import (
    GOLD_UPGRADE_COSTS, PP_UPGRADE_COSTS,
    GADGET_GOLD_COST, STAR_POWER_GOLD_COST, SUPER_RARE_GEAR_GOLD_COST, EPIC_GEAR_GOLD_COST,
    MYTHIC_GEAR_GOLD_COST, HYPERCHARGE_GOLD_COST, BUFFIE_GOLD_COST, BUFFIE_PP_COST
)
from backend.core.models import MetricComparison

def build_comparison(current: int, total: int) -> MetricComparison:
            amount_leftover = max(0, total - current)
            percentage = round((current / total) * 100, 2) if total > 0 else 100.0
            return MetricComparison(
                current=current, 
                total_needed_for_max=total,
                leftover_needed=amount_leftover, 
                percentage_completed=percentage
            )

class PowerLevelCalculator:
    @staticmethod
    def calculate(brawler: Any) -> tuple[int, int]:
        """Returns (invested_gold, invested_pp) for a brawler's current power level."""
        invested_gold = sum(GOLD_UPGRADE_COSTS.get(lvl, 0) for lvl in range(1, brawler.power + 1))
        invested_pp = sum(PP_UPGRADE_COSTS.get(lvl, 0) for lvl in range(1, brawler.power + 1))
        return invested_gold, invested_pp


class AbilitiesCalculator:
    @staticmethod
    def calculate_targets(meta: Dict[str, Any]) -> int:
        """Returns total gold target needed for Gadgets and Star Powers only."""
        return (meta["total_gadgets"] * GADGET_GOLD_COST) + (meta["total_star_powers"] * STAR_POWER_GOLD_COST)

    @staticmethod
    def calculate_current(brawler: Any, meta: Dict[str, Any]) -> int:
        """Returns current gold invested in owned Gadgets and Star Powers only."""
        owned_gadgets = min(len(brawler.gadgets), meta["total_gadgets"])
        owned_star_powers = min(len(brawler.star_powers), meta["total_star_powers"])
        return (owned_gadgets * GADGET_GOLD_COST) + (owned_star_powers * STAR_POWER_GOLD_COST)


class BuffiesCalculator:
    @staticmethod
    def calculate_targets(meta: Dict[str, Any]) -> tuple[int, int]:
        """Returns independent (gold, pp) targets assuming 3 buffie types exist per brawler."""
        if meta.get("has_buffies", True):
            return BUFFIE_GOLD_COST * 3, BUFFIE_PP_COST * 3
        return 0, 0

    @staticmethod
    def calculate_current(brawler: Any, meta: Dict[str, Any]) -> tuple[int, int]:
        """
        Iterates over the individual types of buffies (gadget, starPower, hyperCharge)
        and accumulates costs for every unlocked type.
        """
        if not meta.get("has_buffies", True):
            return 0, 0
            
        buffies_obj = getattr(brawler, "buffies", None)
        if not buffies_obj:
            return 0, 0

        # Convert to dictionary whether it's a Pydantic model or a raw dict
        buffies_dict = buffies_obj.model_dump() if hasattr(buffies_obj, "model_dump") else (
            buffies_obj.__dict__ if hasattr(buffies_obj, "__dict__") else buffies_obj
        )

        # Count how many slots are marked True (e.g., gadget=True, hyperCharge=True)
        unlocked_count = sum(1 for slot, active in buffies_dict.items() if active is True)

        if unlocked_count > 0:
            print(f"[BUFFIE DEBUG] Brawler {brawler.name} has {unlocked_count} active buffies.")
            return (BUFFIE_GOLD_COST * unlocked_count), (BUFFIE_PP_COST * unlocked_count)
            
        return 0, 0

class GearsCalculator:
    @staticmethod
    def calculate_target(meta: Dict[str, Any]) -> int:
        gold = meta["total_super_rare_gears"] * SUPER_RARE_GEAR_GOLD_COST
        if meta["has_epic_gear"]:
            gold += EPIC_GEAR_GOLD_COST
        if meta["has_mythic_gear"]:
            gold += MYTHIC_GEAR_GOLD_COST
        return gold

    @staticmethod
    def calculate_current(brawler: Any) -> int:
        gold = 0
        for gear in brawler.gears:
            gear_name = gear.name.upper()
            if "MYTHIC" in gear_name or "RELOAD" in gear_name:
                gold += MYTHIC_GEAR_GOLD_COST
            elif "EPIC" in gear_name or "SUPER" in gear_name:
                gold += EPIC_GEAR_GOLD_COST
            else:
                gold += SUPER_RARE_GEAR_GOLD_COST
        return gold


class HyperchargeCalculator:
    @staticmethod
    def calculate_target(meta: Dict[str, Any]) -> int:
        return HYPERCHARGE_GOLD_COST if meta["has_hypercharge"] else 0

    @staticmethod
    def calculate_current(brawler: Any, meta: Dict[str, Any]) -> int:
        if meta["has_hypercharge"] and len(brawler.hyper_charges) > 0:
            return HYPERCHARGE_GOLD_COST
        return 0
    
