from app.core.models import PlayerDomain, ProgressionMetrics, MetricComparison

# ==========================================
# 1. BRAWL STARS ECONOMY CONSTANTS
# ==========================================
GOLD_UPGRADE_COSTS = {1: 0, 2: 20, 3: 35, 4: 75, 5: 140, 6: 290, 7: 480, 8: 800, 9: 1250, 10: 1875, 11: 2800}
PP_UPGRADE_COSTS = {1: 0, 2: 20, 3: 30, 4: 50, 5: 80, 6: 130, 7: 210, 8: 340, 9: 550, 10: 890, 11: 1440}

TOTAL_GOLD_TO_MAX_LEVEL = 7765
TOTAL_PP_TO_MAX_LEVEL = 3740

GADGET_GOLD_COST = 1000
STAR_POWER_GOLD_COST = 2000
SUPER_RARE_GEAR_GOLD_COST = 1000
EPIC_GEAR_GOLD_COST = 1500
MYTHIC_GEAR_GOLD_COST = 2000
HYPERCHARGE_GOLD_COST = 5000

# Special Modifier Buffies (Cosmetics/Add-ons)
BUFFIE_GOLD_COST = 1000
BUFFIE_PP_COST = 2000

# ==========================================
# 2. GAME DEFINITION REGISTRY MATRIX
# ==========================================
BRAWLER_REGISTRY_OVERRIDES = {
    "SHELLY": {"has_hypercharge": True, "total_gadgets": 2, "total_star_powers": 2, "total_super_rare_gears": 6, "has_epic_gear": False, "has_mythic_gear": True, "has_buffies": True},
    "COLT": {"has_hypercharge": True, "total_gadgets": 2, "total_star_powers": 2, "total_super_rare_gears": 6, "has_epic_gear": False, "has_mythic_gear": True, "has_buffies": True},
    "BULL": {"has_hypercharge": True, "total_gadgets": 2, "total_star_powers": 2, "total_super_rare_gears": 6, "has_epic_gear": False, "has_mythic_gear": True, "has_buffies": True},
    "BROCK": {"has_hypercharge": True, "total_gadgets": 2, "total_star_powers": 2, "total_super_rare_gears": 6, "has_epic_gear": False, "has_mythic_gear": True, "has_buffies": False},
    "TICK": {"has_hypercharge": True, "total_gadgets": 2, "total_star_powers": 2, "total_super_rare_gears": 6, "has_epic_gear": False, "has_mythic_gear": True, "has_buffies": False},
}

class TrackerAnalyticService:

    @staticmethod
    def calculate_progression_metrics(player: PlayerDomain) -> ProgressionMetrics:
        total_brawlers = len(player.brawlers)
        if total_brawlers == 0:
            raise ValueError("No brawler data found for analytics calculation.")

        # --- Target Goals per Currency ---
        target_power_11_gold = total_brawlers * TOTAL_GOLD_TO_MAX_LEVEL
        target_power_11_pp = total_brawlers * TOTAL_PP_TO_MAX_LEVEL
        
        target_buffies_gold = 0
        target_buffies_pp = 0
        target_gears_gold = 0
        target_hypercharges_gold = 0

        # --- Current Owned Progress per Currency ---
        current_power_11_gold = 0
        current_power_11_pp = 0
        
        current_buffies_gold = 0
        current_buffies_pp = 0
        current_gears_gold = 0
        current_hypercharges_gold = 0

        # Loop through every brawler the player has unlocked
        for brawler in player.brawlers:
            brawler_name_upper = brawler.name.upper()
            
            brawler_meta = BRAWLER_REGISTRY_OVERRIDES.get(brawler_name_upper, {
                "has_hypercharge": True,
                "total_gadgets": 2,
                "total_star_powers": 2,
                "total_super_rare_gears": 5,
                "has_epic_gear": False,
                "has_mythic_gear": False,
                "has_buffies": False
            })

            # --------------------------------------------------------
            # STEP 1: CALCULATE TARGET COSTS FOR THIS BRAWLER
            # --------------------------------------------------------
            # Gadgets & Star Powers (Gold only)
            target_buffies_gold += (brawler_meta["total_gadgets"] * GADGET_GOLD_COST) + (brawler_meta["total_star_powers"] * STAR_POWER_GOLD_COST)
            
            # Additional structural Modifier Buffies (Gold + PP)
            if brawler_meta["has_buffies"]:
                target_buffies_gold += BUFFIE_GOLD_COST
                target_buffies_pp += BUFFIE_PP_COST

            # Gears (Gold only)
            target_gears_gold += (brawler_meta["total_super_rare_gears"] * SUPER_RARE_GEAR_GOLD_COST)
            if brawler_meta["has_epic_gear"]:
                target_gears_gold += EPIC_GEAR_GOLD_COST
            if brawler_meta["has_mythic_gear"]:
                target_gears_gold += MYTHIC_GEAR_GOLD_COST

            # Hypercharges (Gold only)
            if brawler_meta["has_hypercharge"]:
                target_hypercharges_gold += HYPERCHARGE_GOLD_COST

            # --------------------------------------------------------
            # STEP 2: CALCULATE CURRENT ASSETS INVESTED BY THE PLAYER
            # --------------------------------------------------------
            # Base Level Up Costs
            for level in range(1, brawler.power + 1):
                current_power_11_gold += GOLD_UPGRADE_COSTS.get(level, 0)
                current_power_11_pp += PP_UPGRADE_COSTS.get(level, 0)

            # Owned Gadgets and Star Powers (Gold worth)
            owned_gadgets = min(len(brawler.gadgets), brawler_meta["total_gadgets"])
            owned_star_powers = min(len(brawler.star_powers), brawler_meta["total_star_powers"])
            # TODO: Fix buffies calc
            current_buffies_gold += (owned_gadgets * GADGET_GOLD_COST) + (owned_star_powers * STAR_POWER_GOLD_COST)
            
            # Owned Modifier Buffies (Gold + PP worth)
            if brawler_meta["has_buffies"] and brawler.buffies:
                if getattr(brawler.buffies, "unlocked", False) or len(brawler.gears) > 0:
                    current_buffies_gold += BUFFIE_GOLD_COST
                    current_buffies_pp += BUFFIE_PP_COST

            # Owned Gears (Gold worth)
            for gear in brawler.gears:
                gear_name = gear.name.upper()
                if "MYTHIC" in gear_name or "RELOAD" in gear_name:
                    current_gears_gold += MYTHIC_GEAR_GOLD_COST
                elif "EPIC" in gear_name or "SUPER" in gear_name:
                    current_gears_gold += EPIC_GEAR_GOLD_COST
                else:
                    current_gears_gold += SUPER_RARE_GEAR_GOLD_COST

            # Owned Hypercharges (Gold worth)
            if brawler_meta["has_hypercharge"] and len(brawler.hyper_charges) > 0:
                current_hypercharges_gold += HYPERCHARGE_GOLD_COST

        # --------------------------------------------------------
        # STEP 3: CONSTRUCT PROGRESSION ENGINE COMPILATION
        # --------------------------------------------------------
        def build_comparison(current: int, total: int) -> MetricComparison:
            amount_leftover = max(0, total - current)
            percentage = round((current / total) * 100, 2) if total > 0 else 100.0
            return MetricComparison(
                current=current, 
                total_needed_for_max=total,
                leftover_needed=amount_leftover, 
                percentage_completed=percentage
            )

        # 1. Base Level Sub-Reports
        gold_p11_report = build_comparison(current_power_11_gold, target_power_11_gold)
        pp_p11_report = build_comparison(current_power_11_pp, target_power_11_pp)

        # 2. Item/Ability Sub-Reports (Gears, Buffies, Hypercharges)
        gears_report = build_comparison(current_gears_gold, target_gears_gold)
        buffies_report = build_comparison(current_buffies_gold, target_buffies_gold)
        hypercharges_report = build_comparison(current_hypercharges_gold, target_hypercharges_gold)

        # 3. Currency Max Aggregates (Summing all separate gold/pp requirements)
        global_target_gold = target_power_11_gold + target_buffies_gold + target_gears_gold + target_hypercharges_gold
        global_current_gold = current_power_11_gold + current_buffies_gold + current_gears_gold + current_hypercharges_gold
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
            buffies_completion=buffies_report,
            hypercharges_completion=hypercharges_report
        )