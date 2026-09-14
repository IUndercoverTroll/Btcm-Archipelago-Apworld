from __future__ import annotations
from typing import TYPE_CHECKING, Sequence
from BaseClasses import Region, ItemClassification, Location
from . import items

if TYPE_CHECKING:
    from .world import BTCMWorld

from .locations import RHR_table, LFF_table, JS_table, TPS_table, VP_table, \
    CC_table, IR_table, RL_table, TT_table, BB_table, \
    SiSt_table, OK_table, HuHa_table, TFE_table, ToT_table, \
    BotH_table, SwtS_table, SSS_table, LS_table, Minigame_table, BTCMLocation, Three_seed_room_badge_table, \
    Starting_room_badge_table, Observatory_badge_table, TT_badge_table


def create_all_regions(world: BTCMWorld):
    starting_room = Region("Starting Room", world.player, world.multiworld)
    observatory = Region("Observatory", world.player, world.multiworld)
    sinful_starfair = Region("Sinful Starfair", world.player, world.multiworld)
    agamemnon = Region("Agamemnon", world.player, world.multiworld)

    red_hot_reservoir = Region("Red Hot Reservoir", world.player, world.multiworld)
    lonely_floating_farm = Region("Lonely Floating Farm", world.player, world.multiworld)
    jurassic_savanna = Region("Jurassic Savanna", world.player, world.multiworld)
    the_phantom_strider = Region("The Phantom Strider", world.player, world.multiworld)
    virtuaplex = Region("Virtuaplex", world.player, world.multiworld)
    cowboy_canyon = Region("Cowboy Canyon", world.player, world.multiworld)
    immense_residence = Region("Immense Residence", world.player, world.multiworld)
    retroland = Region("Retroland", world.player, world.multiworld)
    thwomp_towers = Region("Thwomp Towers", world.player, world.multiworld)
    blueberg = Region("Blueberg", world.player, world.multiworld)
    #sinful_starfair is already defined above
    orchestral_keys = Region("Orchestral Keys", world.player, world.multiworld)
    hushed_haven = Region("Hushed Haven", world.player, world.multiworld)
    the_final_empire = Region("The Final Empire", world.player, world.multiworld)
    trials_of_terminus = Region("Trials of Terminus", world.player, world.multiworld)

    prehistoric_research_room = Region("Prehistoric Research Room", world.player, world.multiworld)
    three_seed_room = Region("Three Seed Room", world.player, world.multiworld)
    bowser_on_the_highway = Region("Bowser on the Highway", world.player, world.multiworld)
    bowser_secret_shortcut = Region("Bowser's Secret Shortcut", world.player, world.multiworld)
    thwomp_towers_wall_jump = Region("Thwomp Towers Wall Jump", world.player, world.multiworld)
    showdown_with_the_showrunner = Region("Showdown with The Showrunner", world.player, world.multiworld)
    sloppy_shell_sewers = Region("Sloppy Shell Sewers", world.player, world.multiworld)
    lost_city = Region("Lost City", world.player, world.multiworld)

    regions = [starting_room,observatory,sinful_starfair,
               agamemnon,red_hot_reservoir,lonely_floating_farm, jurassic_savanna,
               the_phantom_strider,virtuaplex,cowboy_canyon,immense_residence,
               retroland, thwomp_towers, blueberg, orchestral_keys, hushed_haven, thwomp_towers_wall_jump,
               the_final_empire,trials_of_terminus,prehistoric_research_room,three_seed_room, bowser_secret_shortcut,
               bowser_on_the_highway, showdown_with_the_showrunner, sloppy_shell_sewers, lost_city]

    world.multiworld.regions += regions

    #Only for ruleless connects.
    world.region_dict = {
        starting_room: [red_hot_reservoir],
        prehistoric_research_room: [sloppy_shell_sewers, jurassic_savanna],
        observatory: [cowboy_canyon, immense_residence],
        thwomp_towers_wall_jump: [blueberg],
        sinful_starfair: [showdown_with_the_showrunner],
        agamemnon: [hushed_haven,the_final_empire],
    }

    world.entrance_list = [
        (starting_room, lonely_floating_farm, "One Star Platform"),
        (starting_room, prehistoric_research_room, "Two Star Door"),
        (starting_room, the_phantom_strider, "Eight Star Door"),
        (starting_room, bowser_on_the_highway, "Ten Star Door"),
        (starting_room, virtuaplex, "Virtuaplex Door"),
        (starting_room, bowser_secret_shortcut, "One Seed Door"),
        (starting_room, three_seed_room, "Three Seed Door"),
        (starting_room, observatory, "Telescope"),
        (immense_residence, retroland, "NES"),
        (starting_room, sinful_starfair, "Sinful Starfair Door"),
        (observatory, thwomp_towers, "Thirty Star Cage"),
        (thwomp_towers, lost_city, "Thwomp Guard"),
        (thwomp_towers, thwomp_towers_wall_jump, "Thwomp Towers Wall Jump"),
        (sinful_starfair, agamemnon, "Fifty Star and Six Seed Projector"),
        (agamemnon, orchestral_keys, "Orchestral Keys Koopa Shell"),
        (agamemnon, trials_of_terminus, "Eighteen Star Laser"),
    ]

def connect_regions(world: BTCMWorld, region_dict: dict[Region, list[Region]], entrance_list: Sequence[tuple[Region, Region, str]]):
    #For every value associated with a key, connect the value to the key
    for i in region_dict:
        for j in region_dict[i]:
            i.connect(j)

    for j, k, l in entrance_list:
        j.connect(k,l)

    world.get_region("Red Hot Reservoir").add_locations(RHR_table, BTCMLocation)
    world.get_region("Lonely Floating Farm").add_locations(LFF_table, BTCMLocation)
    world.get_region("Jurassic Savanna").add_locations(JS_table, BTCMLocation)
    world.get_region("The Phantom Strider").add_locations(TPS_table, BTCMLocation)
    world.get_region("Virtuaplex").add_locations(VP_table, BTCMLocation)
    world.get_region("Cowboy Canyon").add_locations(CC_table, BTCMLocation)
    world.get_region("Immense Residence").add_locations(IR_table, BTCMLocation)
    world.get_region("Retroland").add_locations(RL_table, BTCMLocation)
    world.get_region("Thwomp Towers").add_locations(TT_badge_table, BTCMLocation)
    world.get_region("Blueberg").add_locations(BB_table, BTCMLocation)
    world.get_region("Sinful Starfair").add_locations(SiSt_table, BTCMLocation)
    world.get_region("Orchestral Keys").add_locations(OK_table, BTCMLocation)
    world.get_region("Hushed Haven").add_locations(HuHa_table, BTCMLocation)
    world.get_region("The Final Empire").add_locations(TFE_table, BTCMLocation)
    world.get_region("Trials of Terminus").add_locations(ToT_table, BTCMLocation)

    world.get_region("Observatory").add_locations(Minigame_table, BTCMLocation)
    #Separating these 2 because normally when you come in through Bowser's Secret Shortcut you can get all the checks
    #except for the red coin star. That is, unless you do a damage boost onto one of the vehicles, but that feels
    #unintended. Might leave that for logic tricks in the future.
    world.get_region("Bowser on the Highway").add_locations({"Bowser on the Highway Red Coins": 106}, BTCMLocation)
    world.get_region("Bowser's Secret Shortcut").add_locations({"Bowser on the Highway Defeat UrBowser": 107,"Bowser on the Highway Pandora Box": 112,"Bowser on the Highway Lens": 1027}, BTCMLocation)
    world.get_region("Thwomp Towers Wall Jump").add_locations(TT_table, BTCMLocation)
    world.get_region("Showdown with The Showrunner").add_locations(SwtS_table, BTCMLocation)
    world.get_region("Sloppy Shell Sewers").add_locations(SSS_table, BTCMLocation)
    world.get_region("Lost City").add_locations(LS_table, BTCMLocation)

    world.get_region("Starting Room").add_locations(Starting_room_badge_table, BTCMLocation)
    world.get_region("Three Seed Room").add_locations(Three_seed_room_badge_table, BTCMLocation)
    world.get_region("Observatory").add_locations(Observatory_badge_table, BTCMLocation)

def create_event_items(world: BTCMWorld) -> None:
    trial_completion = items.BTCMItem("Trial Completion", ItemClassification.progression, None, world.player)

    world.get_location("RED TRIAL").place_locked_item(trial_completion)
    world.get_location("YELLOW TRIAL").place_locked_item(trial_completion)
    world.get_location("GREEN TRIAL").place_locked_item(trial_completion)
    world.get_location("CYAN TRIAL").place_locked_item(trial_completion)
    world.get_location("BLUE TRIAL").place_locked_item(trial_completion)
    world.get_location("PINK TRIAL").place_locked_item(trial_completion)

