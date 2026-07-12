
from backend.core.models import PlayerDomain, ProgressionMetrics
from backend.core.constants import TOTAL_GOLD_TO_MAX_LEVEL, TOTAL_PP_TO_MAX_LEVEL
from backend.core.registry import BRAWLER_REGISTRY_OVERRIDES, DEFAULT_BRAWLER_ARCHETYPE
from backend.core.services_components import (
    build_comparison, PowerLevelCalculator, AbilitiesCalculator, BuffiesCalculator, GearsCalculator, HyperchargeCalculator
)


class TrackerAnalyticService:
            
    @staticmethod
    def calculate_progression_metrics(player: PlayerDomain) -> ProgressionMetrics:
        total_brawlers = len(player.brawlers)
        if total_brawlers == 0:
            raise ValueError("No brawler data found for analytics calculation.")

        # --- Target Goals per Category ---
        target_power_11_gold = total_brawlers * TOTAL_GOLD_TO_MAX_LEVEL
        target_power_11_pp = total_brawlers * TOTAL_PP_TO_MAX_LEVEL
        target_abilities_gold = 0   # Strictly Gadgets + Star Powers
        target_buffies_gold = 0
        target_buffies_pp = 0     
        target_gears_gold = 0
        target_hypercharges_gold = 0

        # --- Current Owned Progress per Category ---
        current_power_11_gold = current_power_11_pp = 0
        current_abilities_gold = 0
        current_buffies_gold = current_buffies_pp = 0
        current_gears_gold = current_hypercharges_gold = 0

        for brawler in player.brawlers:
            brawler_meta = BRAWLER_REGISTRY_OVERRIDES.get(brawler.name.upper(), DEFAULT_BRAWLER_ARCHETYPE)

            # 1. Targets/Caps Calculations (Strictly Isolated)
            target_abilities_gold += AbilitiesCalculator.calculate_targets(brawler_meta)
            
            b_buffie_t_gold, b_buffie_t_pp = BuffiesCalculator.calculate_targets(brawler_meta)
            target_buffies_gold += b_buffie_t_gold
            print(f"Adding {b_buffie_t_gold} gold to target_buffies_gold for brawler {brawler.name}")
            
            target_buffies_pp += b_buffie_t_pp
            print(f"Adding {b_buffie_t_pp} pp to target_buffies_pp for brawler {brawler.name}")
            print(f"Total gold {target_buffies_gold}, Total pp {target_buffies_pp} after processing brawler {brawler.name}")

            target_gears_gold += GearsCalculator.calculate_target(brawler_meta)
            target_hypercharges_gold += HyperchargeCalculator.calculate_target(brawler_meta)

            # 2. Current Asset Investment Calculations
            brawler_level_gold, brawler_level_pp = PowerLevelCalculator.calculate(brawler)
            current_power_11_gold += brawler_level_gold
            current_power_11_pp += brawler_level_pp

            current_abilities_gold += AbilitiesCalculator.calculate_current(brawler, brawler_meta)

            b_buffie_c_gold, b_buffie_c_pp = BuffiesCalculator.calculate_current(brawler, brawler_meta)
            print("------------------------------------------------------ ")
            print(f"Adding {b_buffie_c_gold} gold to current_buffies_gold for brawler {brawler.name}")
            print(f"Adding {b_buffie_c_pp} pp to current_buffies_pp for brawler {brawler.name}")
            print(f"Total gold {current_buffies_gold}, Total pp {current_buffies_pp} after processing brawler {brawler.name}")

            current_buffies_gold += b_buffie_c_gold
            current_buffies_pp += b_buffie_c_pp

            current_gears_gold += GearsCalculator.calculate_current(brawler)
            current_hypercharges_gold += HyperchargeCalculator.calculate_current(brawler, brawler_meta)

        # 3. Build Independent Reports
        gold_p11_report = build_comparison(current_power_11_gold, target_power_11_gold)
        pp_p11_report = build_comparison(current_power_11_pp, target_power_11_pp)
        gears_report = build_comparison(current_gears_gold, target_gears_gold)
        buffies_gold_report = build_comparison(current_buffies_gold, target_buffies_gold)
        buffies_pp_report = build_comparison(current_buffies_pp, target_buffies_pp)
        hypercharges_report = build_comparison(current_hypercharges_gold, target_hypercharges_gold)

        # 4. Global Compound Aggregates (Including BOTH abilities and independent buffies values)
        global_target_gold = (target_power_11_gold + target_abilities_gold + 
                              target_buffies_gold + target_gears_gold + target_hypercharges_gold)
        
        global_current_gold = (current_power_11_gold + current_abilities_gold + 
                               current_buffies_gold + current_gears_gold + current_hypercharges_gold)
        
        gold_max_report = build_comparison(global_current_gold, global_target_gold)

        global_target_pp = target_power_11_pp + target_buffies_pp
        global_current_pp = current_power_11_pp + current_buffies_pp
        pp_max_report = build_comparison(global_current_pp, global_target_pp)
        
        return ProgressionMetrics(
            gold_max=gold_max_report,
            pp_max=pp_max_report,
            gold_power_11_only=gold_p11_report,
            pp_power_11_only=pp_p11_report,
            gears_completion=gears_report,
            buffies_gold=buffies_gold_report,
            buffies_pp=buffies_pp_report,
            hypercharges_completion=hypercharges_report
        )