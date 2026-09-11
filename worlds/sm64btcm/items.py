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
    #They're calling him the YandereDev of Archipelago
    item_pool.append(world.create_item("Lens"))
    item_pool.append(world.create_item("Starfair Key"))
    item_pool.append(world.create_item("Rocket Boots"))
    item_pool.append(world.create_item("Pandora Boxes"))
    item_pool.append(world.create_item("Vanetal Cap"))
    item_pool.append(world.create_item("Koopa Shell"))
    item_pool.append(world.create_item("Save Shatter Burden"))
    item_pool.append(world.create_item("Withering Burden"))
    item_pool.append(world.create_item("Brittle Burden"))
    item_pool.append(world.create_item("Boss Slayer Badge"))
    item_pool.append(world.create_item("Bottomless Badge"))
    item_pool.append(world.create_item("Heal Plus Badge"))
    item_pool.append(world.create_item("Fast Foot Badge"))
    item_pool.append(world.create_item("Sticky Badge"))
    item_pool.append(world.create_item("Weight Badge"))
    item_pool.append(world.create_item("Feather Badge"))
    item_pool.append(world.create_item("Squish Badge"))
    item_pool.append(world.create_item("Burn Badge"))
    item_pool.append(world.create_item("Star Radar Badge"))
    item_pool.append(world.create_item("Magnet Badge"))
    item_pool.append(world.create_item("Double Time Badge"))
    item_pool.append(world.create_item("Greed Badge"))
    item_pool.append(world.create_item("Mana Regen Badge"))
    item_pool.append(world.create_item("HP Regen Badge"))
    item_pool.append(world.create_item("Fins Badge"))
    item_pool.append(world.create_item("Gills Badge"))
    item_pool.append(world.create_item("Double Damage Badge"))
    item_pool.append(world.create_item("Defense Badge"))
    item_pool.append(world.create_item("Fall Damage Badge"))
    item_pool.append(world.create_item("Lava Boost Badge"))



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