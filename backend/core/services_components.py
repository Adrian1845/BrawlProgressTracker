from __future__ import annotations

from typing import Any, Dict

from core.constants import (
    BUFFIE_GOLD_COST,
    BUFFIE_PP_COST,
    EPIC_GEAR_GOLD_COST,
    GADGET_GOLD_COST,
    GOLD_UPGRADE_COSTS,
    HYPERCHARGE_GOLD_COST,
    MYTHIC_GEAR_GOLD_COST,
    PP_UPGRADE_COSTS,
    STAR_POWER_GOLD_COST,
    SUPER_RARE_GEAR_GOLD_COST,
)
from core.models import MetricComparison


def build_comparison(current: int, total: int) -> MetricComparison:
    amount_leftover = max(0, total - current)
    percentage = round((current / total) * 100, 2) if total > 0 else 100.0
    return MetricComparison(
        current=current,
        total_needed_for_max=total,
        leftover_needed=amount_leftover,
        percentage_completed=percentage,
    )


class PowerLevelCalculator:
    @staticmethod
    def calculate(brawler: Any) -> tuple[int, int]:
        """Returns (invested_gold, invested_pp) for a brawler's current power level."""
        invested_gold = sum(GOLD_UPGRADE_COSTS.get(lvl, 0) for lvl in range(1, brawler.power + 1))
        invested_pp = sum(PP_UPGRADE_COSTS.get(lvl, 0) for lvl in range(1, brawler.power + 1))
        return invested_gold, invested_pp


class GadgetCalculator:
    @staticmethod
    def calculate_target_count(meta: Dict[str, Any]) -> int:
        return meta.get("total_gadgets", 0)

    @staticmethod
    def calculate_target_gold(meta: Dict[str, Any]) -> int:
        return meta.get("total_gadgets", 0) * GADGET_GOLD_COST

    @staticmethod
    def calculate_current_count(brawler: Any, meta: Dict[str, Any]) -> int:
        total_gadgets = meta.get("total_gadgets", 0)
        return min(len(getattr(brawler, "gadgets", []) or []), total_gadgets)

    @staticmethod
    def calculate_current_gold(brawler: Any, meta: Dict[str, Any]) -> int:
        return GadgetCalculator.calculate_current_count(brawler, meta) * GADGET_GOLD_COST


class StarPowerCalculator:
    @staticmethod
    def calculate_target_count(meta: Dict[str, Any]) -> int:
        return meta.get("total_star_powers", 0)

    @staticmethod
    def calculate_target_gold(meta: Dict[str, Any]) -> int:
        return meta.get("total_star_powers", 0) * STAR_POWER_GOLD_COST

    @staticmethod
    def calculate_current_count(brawler: Any, meta: Dict[str, Any]) -> int:
        total_star_powers = meta.get("total_star_powers", 0)
        return min(len(getattr(brawler, "star_powers", []) or []), total_star_powers)

    @staticmethod
    def calculate_current_gold(brawler: Any, meta: Dict[str, Any]) -> int:
        return StarPowerCalculator.calculate_current_count(brawler, meta) * STAR_POWER_GOLD_COST


class BuffiesCalculator:
    @staticmethod
    def calculate_target_count(meta: Dict[str, Any]) -> int:
        return 3 if meta.get("has_buffies", True) else 0

    @staticmethod
    def calculate_targets(meta: Dict[str, Any]) -> tuple[int, int]:
        """Returns independent (gold, pp) targets assuming 3 buffie types exist per brawler."""
        if not meta.get("has_buffies", True):
            return 0, 0
        return BUFFIE_GOLD_COST * 3, BUFFIE_PP_COST * 3

    @staticmethod
    def calculate_current_count(brawler: Any, meta: Dict[str, Any]) -> int:
        if not meta.get("has_buffies", True):
            return 0

        buffies_obj = getattr(brawler, "buffies", None)
        if not buffies_obj:
            return 0

        buffies_dict = buffies_obj.model_dump() if hasattr(buffies_obj, "model_dump") else (
            buffies_obj.__dict__ if hasattr(buffies_obj, "__dict__") else buffies_obj
        )
        return sum(1 for slot, active in buffies_dict.items() if active is True)

    @staticmethod
    def calculate_current(brawler: Any, meta: Dict[str, Any]) -> tuple[int, int]:
        if not meta.get("has_buffies", True):
            return 0, 0

        unlocked_count = BuffiesCalculator.calculate_current_count(brawler, meta)
        return (BUFFIE_GOLD_COST * unlocked_count), (BUFFIE_PP_COST * unlocked_count)


class GearsCalculator:
    @staticmethod
    def calculate_target_count(meta: Dict[str, Any]) -> int:
        total = meta.get("total_super_rare_gears", 0)
        if meta.get("has_epic_gear"):
            total += 1
        if meta.get("has_mythic_gear"):
            total += 1
        return total

    @staticmethod
    def calculate_target(meta: Dict[str, Any]) -> int:
        gold = meta.get("total_super_rare_gears", 0) * SUPER_RARE_GEAR_GOLD_COST
        if meta.get("has_epic_gear"):
            gold += EPIC_GEAR_GOLD_COST
        if meta.get("has_mythic_gear"):
            gold += MYTHIC_GEAR_GOLD_COST
        return gold

    @staticmethod
    def calculate_current_count(brawler: Any) -> int:
        return len(getattr(brawler, "gears", []) or [])

    @staticmethod
    def calculate_current(brawler: Any) -> int:
        gold = 0
        for gear in getattr(brawler, "gears", []) or []:
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
    def calculate_target_count(meta: Dict[str, Any]) -> int:
        return 1 if meta.get("has_hypercharge") else 0

    @staticmethod
    def calculate_target(meta: Dict[str, Any]) -> int:
        return HYPERCHARGE_GOLD_COST if meta.get("has_hypercharge") else 0

    @staticmethod
    def calculate_current_count(brawler: Any, meta: Dict[str, Any]) -> int:
        if not meta.get("has_hypercharge"):
            return 0
        return 1 if len(getattr(brawler, "hyper_charges", []) or []) > 0 else 0

    @staticmethod
    def calculate_current(brawler: Any, meta: Dict[str, Any]) -> int:
        if meta.get("has_hypercharge") and len(getattr(brawler, "hyper_charges", []) or []) > 0:
            return HYPERCHARGE_GOLD_COST
        return 0
