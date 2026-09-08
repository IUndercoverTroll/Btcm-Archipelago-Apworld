from BaseClasses import Region

from .locations import RHR_table,LFF_table,JS_table,TPS_table,VP_table, \
    CC_table,IR_table,RL_table,TT_table,BB_table, \
    SiSt_table,OK_table,HuHa_table,TFE_table,ToT_table, \
    BotH_table,SwtS_table,SSS_table,LS_table,Minigame_table, BTCMLocation

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
    bowser_on_the_highway = Region("Bowser on The Highway", world.player, world.multiworld)
    showdown_with_the_showrunner = Region("Showdown with The Showrunner", world.player, world.multiworld)
    sloppy_shell_sewers = Region("Sloppy Shell Sewers", world.player, world.multiworld)
    lost_city = Region("Lost City", world.player, world.multiworld)

    regions = [starting_room,observatory,sinful_starfair,
               agamemnon,red_hot_reservoir,lonely_floating_farm, jurassic_savanna,
               the_phantom_strider,virtuaplex,cowboy_canyon,immense_residence,
               retroland, thwomp_towers, blueberg, orchestral_keys, hushed_haven,
               the_final_empire,trials_of_terminus,prehistoric_research_room,bowser_on_the_highway,
               showdown_with_the_showrunner, sloppy_shell_sewers, lost_city]

    world.multiworld.regions += regions

    world.region_dict = {
        starting_room: [red_hot_reservoir, lonely_floating_farm,the_phantom_strider, virtuaplex,
                        sinful_starfair,observatory,prehistoric_research_room,bowser_on_the_highway],
        prehistoric_research_room: [sloppy_shell_sewers, jurassic_savanna],
        observatory: [cowboy_canyon, immense_residence, thwomp_towers],
        immense_residence: [retroland],
        thwomp_towers: [blueberg, lost_city],
        sinful_starfair: [showdown_with_the_showrunner,agamemnon],
        agamemnon: [orchestral_keys, hushed_haven,the_final_empire,trials_of_terminus],
    }

def connect_regions(world: BTCMWorld, region_dict: dict):
    #For every value associated with a key, connect the value to the key
    for i in region_dict:
        for j in region_dict[i]:
            i.connect(j)

    world.get_region("Red Hot Reservoir").add_locations(RHR_table, BTCMLocation)
    world.get_region("Lonely Floating Farm").add_locations(LFF_table, BTCMLocation)
    world.get_region("Jurassic Savanna").add_locations(JS_table, BTCMLocation)
    world.get_region("The Phantom Strider").add_locations(TPS_table, BTCMLocation)
    world.get_region("Virtuaplex").add_locations(VP_table, BTCMLocation)
    world.get_region("Cowboy Canyon").add_locations(CC_table, BTCMLocation)
    world.get_region("Immense Residence").add_locations(IR_table, BTCMLocation)
    world.get_region("Retroland").add_locations(RL_table, BTCMLocation)
    world.get_region("Thwomp Towers").add_locations(TT_table, BTCMLocation)
    world.get_region("Blueberg").add_locations(BB_table, BTCMLocation)
    world.get_region("Sinful Starfair").add_locations(SiSt_table, BTCMLocation)
    world.get_region("Orchestral Keys").add_locations(OK_table, BTCMLocation)
    world.get_region("Hushed Haven").add_locations(HuHa_table, BTCMLocation)
    world.get_region("The Final Empire").add_locations(TFE_table, BTCMLocation)
    world.get_region("Trials of Terminus").add_locations(ToT_table, BTCMLocation)

    world.get_region("Observatory").add_locations(Minigame_table, BTCMLocation)
    world.get_region("Bowser on the Highway").add_locations(BotH_table, BTCMLocation)
    world.get_region("Showdown with the Showrunner").add_locations(SwtS_table, BTCMLocation)
    world.get_region("Sloppy Shell Sewers").add_locations(SSS_table, BTCMLocation)
    world.get_region("Lost City").add_locations(LS_table, BTCMLocation)