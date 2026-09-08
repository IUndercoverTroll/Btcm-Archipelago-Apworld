from ..AutoWorld import World
from . import items, locations, region

class BTCMWorld(World):
    """Super Mario 64: Beyond the Cursed Mirror is a romhack of SM64 with a new story as well as the ability to level up, badges, and costumes."""
    game = "Super Mario 64: Beyond the Cursed Mirror"

    location_name_to_id = locations.location_table
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Starting Room"

    def create_regions(self) -> None:
        region.create_all_regions(self)
        region.connect_regions(self, self.region_dict)

    def set_rules(self) -> None:
        pass

    def create_items(self) -> None:
        items.create_item_pool(self)

    def create_item(self, name: str) -> items.BTCMItem:
        return items.create_single_item(self, name)
    
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)