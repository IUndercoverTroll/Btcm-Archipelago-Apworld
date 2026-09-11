from __future__ import annotations
from BaseClasses import ItemClassification, Item
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .world import BTCMWorld

class BTCMItem(Item):
    game = "Super Mario 64: Beyond the Cursed Mirror"

ITEM_NAME_TO_ID = {
    "Power Star": 1,
    "Cosmic Seed": 2,
    "Blue Star": 3,
    "Lens": 4,
    "Starfair Key": 5,
    "Rocket Boots": 6,
    "Pandora Boxes": 7,
    "Vanetal Cap": 8,
    "Koopa Shell": 9,
    "Wallet": 10,
    "Lava Boost Badge": 11,
    "Fall Damage Badge": 12,
    "Defense Badge": 13,
    "Double Damage Badge": 14,
    "Gills Badge": 15,
    "Fins Badge": 16,
    "HP Regen Badge": 17,
    "Mana Regen Badge": 18,
    "Greed Badge": 19,
    "Double Time Badge": 20,
    "Magnet Badge": 21,
    "Star Radar Badge": 22,
    "Burn Badge": 23,
    "Squish Badge": 24,
    "Feather Badge": 25,
    "Weight Badge": 26,
    "Sticky Badge": 27,
    "Fast Foot Badge": 28,
    "Heal Plus Badge": 29,
    "Bottomless Badge": 30,
    "Boss Slayer Badge": 31,
    "Brittle Burden": 32,
    "Withering Burden": 33,
    "Save Shatter Burden": 34,
    "Fire Flower Costume": 35,
    "Glitchy Costume": 36,
    "Luigi Costume": 37,
    "Wario Costume": 38,
    "Disco Costume": 39,
    "Undead Pirate Costume": 40,
    "Mocap Costume": 41,
    "Darius Costume": 42,
    "Butler Costume": 43,
    "Retro Costume": 44,
    "Thwomp Costume": 45,
    "Builder Costume": 46,
    "Showrunner Costume": 47,
    "Cosmic Phantasm Costume": 48,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Power Star": ItemClassification.progression_deprioritized_skip_balancing,
    "Cosmic Seed": ItemClassification.progression_deprioritized_skip_balancing,
    "Blue Star": ItemClassification.filler,
    "Lens": ItemClassification.progression,
    "Starfair Key": ItemClassification.progression,
    "Rocket Boots": ItemClassification.progression,
    "Pandora Boxes": ItemClassification.progression,
    "Vanetal Cap": ItemClassification.progression,
    "Koopa Shell": ItemClassification.progression,
    "Wallet": ItemClassification.progression,
    "Save Shatter Burden": ItemClassification.filler,
    "Withering Burden": ItemClassification.filler,
    "Brittle Burden": ItemClassification.filler,
    "Boss Slayer Badge": ItemClassification.useful,
    "Bottomless Badge": ItemClassification.useful,
    "Heal Plus Badge": ItemClassification.useful,
    "Fast Foot Badge": ItemClassification.useful,
    "Sticky Badge": ItemClassification.useful | ItemClassification.progression,
    "Weight Badge": ItemClassification.useful,
    "Feather Badge": ItemClassification.useful | ItemClassification.progression,
    "Squish Badge": ItemClassification.useful,
    "Burn Badge": ItemClassification.useful,
    "Star Radar Badge": ItemClassification.useful,
    "Magnet Badge": ItemClassification.useful,
    "Double Time Badge": ItemClassification.useful | ItemClassification.progression,
    "Greed Badge": ItemClassification.useful,
    "Mana Regen Badge": ItemClassification.useful,
    "HP Regen Badge": ItemClassification.useful,
    "Fins Badge": ItemClassification.useful,
    "Gills Badge": ItemClassification.useful,
    "Double Damage Badge": ItemClassification.useful,
    "Defense Badge": ItemClassification.useful,
    "Fall Damage Badge": ItemClassification.useful,
    "Lava Boost Badge": ItemClassification.useful | ItemClassification.progression,
    "Fire Flower Costume": ItemClassification.filler,
    "Glitchy Costume": ItemClassification.filler,
    "Luigi Costume": ItemClassification.filler,
    "Wario Costume": ItemClassification.filler,
    "Disco Costume": ItemClassification.filler,
    "Undead Pirate Costume": ItemClassification.filler,
    "Mocap Costume": ItemClassification.filler,
    "Darius Costume": ItemClassification.filler,
    "Butler Costume": ItemClassification.filler,
    "Retro Costume": ItemClassification.filler,
    "Thwomp Costume": ItemClassification.filler,
    "Builder Costume": ItemClassification.filler,
    "Showrunner Costume": ItemClassification.filler,
    "Cosmic Phantasm Costume": ItemClassification.filler,
}

#Some bits of this Stolen directly from the APQuest archipelago
def create_item_pool(world: BTCMWorld):
    item_pool = []

    for _ in range(80):
        item_pool.append(world.create_item("Power Star"))
    for _ in range(40):
        item_pool.append(world.create_item("Cosmic Seed"))
    for _ in range(11):
        item_pool.append(world.create_item("Wallet"))
    for key in ITEM_NAME_TO_ID:
        if ITEM_NAME_TO_ID[key] < 4 or ITEM_NAME_TO_ID[key] == 10:
            continue
        item_pool.append(world.create_item(key))

    number_of_items = len(item_pool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    item_pool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += item_pool

def create_single_item(world: BTCMWorld, name: str) -> BTCMItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return BTCMItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def get_random_filler_item_name(world: BTCMWorld) -> str:
    return "Blue Star"