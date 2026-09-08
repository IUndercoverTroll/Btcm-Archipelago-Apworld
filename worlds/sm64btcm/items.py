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
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Power Star": ItemClassification.progression_deprioritized_skip_balancing,
    "Cosmic Seed": ItemClassification.progression_deprioritized_skip_balancing,
    "Blue Star": ItemClassification.filler,
}

#Some bits of this Stolen directly from the APQuest archipelago
def create_item_pool(world: BTCMWorld):
    item_pool = []

    for i in range(80):
        item_pool.append(world.create_item("Power Star"))
    for i in range(40):
        item_pool.append(world.create_item("Cosmic Seed"))


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