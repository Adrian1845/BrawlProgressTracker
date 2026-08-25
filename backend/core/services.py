from core.constants import TOTAL_GOLD_TO_MAX_LEVEL, TOTAL_PP_TO_MAX_LEVEL
from core.models import PlayerDomain, ProgressMetricGroup, ProgressionMetricsV2
from core.registry import BRAWLER_REGISTRY_OVERRIDES, DEFAULT_BRAWLER_ARCHETYPE
from core.services_components import (
    BuffiesCalculator,
    GadgetCalculator,
    GearsCalculator,
    HyperchargeCalculator,
    PowerLevelCalculator,
    StarPowerCalculator,
    build_comparison,
)


class TrackerAnalyticService:
    @staticmethod
    def calculate_progression_metrics(player: PlayerDomain) -> ProgressionMetricsV2:
        total_brawlers = len(player.brawlers)
        if total_brawlers == 0:
            raise ValueError("No brawler data found for analytics calculation.")

        # --- Targets / current totals ---
        target_power_11_gold = total_brawlers * TOTAL_GOLD_TO_MAX_LEVEL
        target_power_11_pp = total_brawlers * TOTAL_PP_TO_MAX_LEVEL
        current_power_11_gold = 0
        current_power_11_pp = 0
        current_power_11_count = 0

        target_gadget_count = 0
        target_gadget_gold = 0
        current_gadget_count = 0
        current_gadget_gold = 0

        target_star_power_count = 0
        target_star_power_gold = 0
        current_star_power_count = 0
        current_star_power_gold = 0

        target_gears_count = 0
        target_gears_gold = 0
        current_gears_count = 0
        current_gears_gold = 0

        target_hypercharges_count = 0
        target_hypercharges_gold = 0
        current_hypercharges_count = 0
        current_hypercharges_gold = 0

        target_buffies_count = 0
        target_buffies_gold = 0
        target_buffies_pp = 0
        current_buffies_count = 0
        current_buffies_gold = 0
        current_buffies_pp = 0

        for brawler in player.brawlers:
            brawler_meta = BRAWLER_REGISTRY_OVERRIDES.get(
                brawler.name.upper(),
                DEFAULT_BRAWLER_ARCHETYPE,
            )

            # Power 11 progress
            if brawler.power == 11:
                current_power_11_count += 1
            brawler_level_gold, brawler_level_pp = PowerLevelCalculator.calculate(brawler)
            current_power_11_gold += brawler_level_gold
            current_power_11_pp += brawler_level_pp

            # Gadgets
            target_gadget_count += GadgetCalculator.calculate_target_count(brawler_meta)
            target_gadget_gold += GadgetCalculator.calculate_target_gold(brawler_meta)
            current_gadget_count += GadgetCalculator.calculate_current_count(brawler, brawler_meta)
            current_gadget_gold += GadgetCalculator.calculate_current_gold(brawler, brawler_meta)

            # Star powers
            target_star_power_count += StarPowerCalculator.calculate_target_count(brawler_meta)
            target_star_power_gold += StarPowerCalculator.calculate_target_gold(brawler_meta)
            current_star_power_count += StarPowerCalculator.calculate_current_count(brawler, brawler_meta)
            current_star_power_gold += StarPowerCalculator.calculate_current_gold(brawler, brawler_meta)

            # Gears
            target_gears_count += GearsCalculator.calculate_target_count(brawler_meta)
            target_gears_gold += GearsCalculator.calculate_target(brawler_meta)
            current_gears_count += GearsCalculator.calculate_current_count(brawler)
            current_gears_gold += GearsCalculator.calculate_current(brawler)

            # Hypercharges
            target_hypercharges_count += HyperchargeCalculator.calculate_target_count(brawler_meta)
            target_hypercharges_gold += HyperchargeCalculator.calculate_target(brawler_meta)
            current_hypercharges_count += HyperchargeCalculator.calculate_current_count(brawler, brawler_meta)
            current_hypercharges_gold += HyperchargeCalculator.calculate_current(brawler, brawler_meta)

            # Buffies
            b_buffie_t_gold, b_buffie_t_pp = BuffiesCalculator.calculate_targets(brawler_meta)
            target_buffies_count += BuffiesCalculator.calculate_target_count(brawler_meta)
            target_buffies_gold += b_buffie_t_gold
            target_buffies_pp += b_buffie_t_pp

            b_buffie_c_gold, b_buffie_c_pp = BuffiesCalculator.calculate_current(brawler, brawler_meta)
            current_buffies_count += BuffiesCalculator.calculate_current_count(brawler, brawler_meta)
            current_buffies_gold += b_buffie_c_gold
            current_buffies_pp += b_buffie_c_pp

        gold_p11_report = build_comparison(current_power_11_gold, target_power_11_gold)
        pp_p11_report = build_comparison(current_power_11_pp, target_power_11_pp)
        gears_report = build_comparison(current_gears_gold, target_gears_gold)
        buffies_gold_report = build_comparison(current_buffies_gold, target_buffies_gold)
        buffies_pp_report = build_comparison(current_buffies_pp, target_buffies_pp)
        hypercharges_report = build_comparison(current_hypercharges_gold, target_hypercharges_gold)

        global_target_gold = (
            target_power_11_gold
            + target_gadget_gold
            + target_star_power_gold
            + target_gears_gold
            + target_hypercharges_gold
            + target_buffies_gold
        )
        global_current_gold = (
            current_power_11_gold
            + current_gadget_gold
            + current_star_power_gold
            + current_gears_gold
            + current_hypercharges_gold
            + current_buffies_gold
        )
        gold_max_report = build_comparison(global_current_gold, global_target_gold)

        global_target_pp = target_power_11_pp + target_buffies_pp
        global_current_pp = current_power_11_pp + current_buffies_pp
        pp_max_report = build_comparison(global_current_pp, global_target_pp)

        return ProgressionMetricsV2(
            max_level=ProgressMetricGroup(
                gold=gold_max_report,
                pp=pp_max_report,
            ),
            power_11=ProgressMetricGroup(
                count=build_comparison(current_power_11_count, total_brawlers),
                gold=gold_p11_report,
                pp=pp_p11_report,
            ),
            gadgets=ProgressMetricGroup(
                count=build_comparison(current_gadget_count, target_gadget_count),
                gold=build_comparison(current_gadget_gold, target_gadget_gold),
            ),
            star_powers=ProgressMetricGroup(
                count=build_comparison(current_star_power_count, target_star_power_count),
                gold=build_comparison(current_star_power_gold, target_star_power_gold),
            ),
            gears=ProgressMetricGroup(
                count=build_comparison(current_gears_count, target_gears_count),
                gold=gears_report,
            ),
            buffies=ProgressMetricGroup(
                count=build_comparison(current_buffies_count, target_buffies_count),
                gold=buffies_gold_report,
                pp=buffies_pp_report,
            ),
            hypercharges=ProgressMetricGroup(
                count=build_comparison(current_hypercharges_count, target_hypercharges_count),
                gold=hypercharges_report,
            ),
        )
