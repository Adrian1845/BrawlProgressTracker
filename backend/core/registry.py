from typing import Dict, Any

DEFAULT_BRAWLER_ARCHETYPE = {
    "has_hypercharge": True,
    "total_gadgets": 2,
    "total_star_powers": 2,
    "total_super_rare_gears": 6,
    "has_epic_gear": False,
    "has_mythic_gear": False,
    "has_buffies": True
}

MYTHIC_GEAR_OWNERS = {"TICK", "PAM", "GENE", "EVE", "SANDY", "AMBER"}
EPIC_GEAR_OWNERS = {"EL PRIMO", "JESSIE", "PENNY", "JACKY", "NANI", "BONNIE", "BELLE", "ASH", "LOLA", "TARA", "MR. P", "SPROUT", "LOU", "EVE", "OTIS", "AMBER"}
NO_HYPERCHARGE_YET = {"NORI"}
NO_BUFFIES_YET = {"EL PRIMO", "BARLEY", "POCO", "ROSA", "JESSIE", "DYNAMIKE", "TICK", "DARRYL", "PENNY", "CARL", "JACKY", "GUS",
                "STU", "PIPER", "PAM", "BEA", "NANI", "GROM", "BONNIE", "GALE", "BELLE", "ASH", "LOLA", "SAM", "MANDY", "MAISIE", "HANK", "PEARL", "LARRY & LAWRIE", 
                "ANGELO", "BERRY", "SHADE", "MEEPLE", "TRUNK", "BOLT", "TARA", "GENE", "MR. P", "SPROUT", "BYRON", "SQUEAK", "LOU", "RUFFS",
                "BUZZ", "FANG", "EVE", "JANET", "OTIS", "BUSTER", "GRAY", "R-T", "WILLOW", "DOUG", "CHUCK", "CHARLIE", "MICO", "MELODIE", "LILY", "CLANCY", "MOE", "JUJU",
                "OLLIE", "LUMI", "FINX", "JAE-YONG", "ALLI", "MINA", "ZIGGY", "GIGI", "NAJIA", "GLOWY", "STARR NOVA", "DAMIAN", "SANDY", "AMBER", "CHESTER",
                "CORDELIUS", "KIT", "DRACO", "KENJI", "PIERCE", "KAZE","SIRIUS"}

BRAWLER_MASTER_NAMES = [
    # Trophy Road & Rares
    "SHELLY", "NITA", "COLT", "BULL", "BROCK", "EL PRIMO", "BARLEY", "POCO", "ROSA", 
    # Super Rares
    "JESSIE", "DYNAMIKE", "TICK", "8-BIT", "RICO", "DARRYL", "PENNY", "CARL", "JACKY", "GUS",
    # Epics
    "BO", "EMZ", "STU", "PIPER", "PAM", "FRANK", "BIBI", "BEA", "NANI", "EDGAR", "GRIFF", 
    "GROM", "BONNIE", "GALE", "COLETTE", "BELLE", "ASH", "LOLA", "SAM", "MANDY", "MAISIE", 
    "HANK", "PEARL", "LARRY & LAWRIE", "ANGELO", "BERRY", "SHADE", "MEEPLE", "TRUNK", "BOLT",
    # Mythics
    "MORTIS", "TARA", "GENE", "MAX", "MR. P", "SPROUT", "BYRON", "SQUEAK", "LOU", "RUFFS", 
    "BUZZ", "FANG", "EVE", "JANET", "OTIS", "BUSTER", "GRAY", "R-T", "WILLOW", "DOUG", 
    "CHUCK", "CHARLIE", "MICO", "MELODIE", "LILY", "CLANCY", "MOE", "JUJU", "OLLIE", 
    "LUMI", "FINX", "JAE-YONG", "ALLI", "MINA", "ZIGGY", "GIGI", "NAJIA", "GLOWY", "STARR NOVA", "DAMIAN",
    # Legendaries & Ultra Legendaries
    "SPIKE", "CROW", "LEON", "SANDY", "AMBER", "MEG", "SURGE", "CHESTER", "CORDELIUS", 
    "KIT", "DRACO", "KENJI", "PIERCE", "KAZE", "SIRIUS", "NORI"
]

def generate_brawler_registry() -> Dict[str, Dict[str, Any]]:
    """
    Programmatically builds a complete registry map for every brawler
    """
    registry = {}
    for name in BRAWLER_MASTER_NAMES:
        # Copy the clean template base mapping
        brawler_config = DEFAULT_BRAWLER_ARCHETYPE.copy()
        
        # Inject dynamic rules/exceptions
        if name in MYTHIC_GEAR_OWNERS:
            brawler_config["has_mythic_gear"] = True
            brawler_config["total_super_rare_gears"] = 6
            
        if name in EPIC_GEAR_OWNERS:
            brawler_config["has_epic_gear"] = True
            
        if name in NO_HYPERCHARGE_YET:
            brawler_config["has_hypercharge"] = False
            
        if name in NO_BUFFIES_YET:
            brawler_config["has_buffies"] = False
            
        registry[name] = brawler_config
        
    return registry

BRAWLER_REGISTRY_OVERRIDES = generate_brawler_registry()