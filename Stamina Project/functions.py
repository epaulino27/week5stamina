import random

def stamina_adjustment(terrain):
    adjustments = {
        "Foragers Forest": random.randint(10, 25),     # Randomly adjust between 10 and 25 for Foragers Forest
        "Mystical Mountain": random.randint(0, 10),  # Randomly adjust between 0 and 10 for Mystical Mountain
        "Savage Swamp": random.randint(-25, -10),     # Randomly adjust between -35 and -25 for Savage Swamp
        "Treacherous Tundra": random.randint(-35, -20)      # Randomly adjust between -35 and -20 for Treacherous Tundra
    }
    return adjustments.get(terrain, 0)