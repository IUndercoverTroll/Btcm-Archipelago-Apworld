from rule_builder.rules import Has, HasAllCounts, CanReachLocation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import BTCMWorld

def set_entrance_rules(world: 'BTCMWorld'):
    world.set_rule(world.get_entrance("One Star Platform"),Has("Power Star"))
    world.set_rule(world.get_entrance("Two Star Door"), Has("Power Star", count=2))
    world.set_rule(world.get_entrance("Eight Star Door"), Has("Power Star", count=8))
    world.set_rule(world.get_entrance("Ten Star Door"), Has("Power Star", count=10))
    world.set_rule(world.get_entrance("Virtuaplex Door"), CanReachLocation("Bowser on the Highway Defeat UrBowser"))
    world.set_rule(world.get_entrance("One Seed Door"), Has("Power Star", count=10) | Has("Cosmic Seed"))
    world.set_rule(world.get_entrance("Three Seed Door"), Has("Cosmic Seed", count=3))
    world.set_rule(world.get_entrance("Telescope"), Has("Lens") & Has("Power Star"))
    world.set_rule(world.get_entrance("NES"), CanReachLocation("IR: QUEST FOR CHEESE"))
    world.set_rule(world.get_entrance("Sinful Starfair Door"), Has("Starfair Key"))
    world.set_rule(world.get_entrance("Thirty Star Cage"), Has("Power Star", count=30))
    world.set_rule(world.get_entrance("Thwomp Guard"), CanReachLocation("TT: DUEL THE THWOMP KING"))
    world.set_rule(world.get_entrance("Thwomp Towers Wall Jump"), Has("Sticky Badge")) #Pretty much every star requires that one wall jump which imo isn't that hard, but I can imagine people struggling without it.
    world.set_rule(world.get_entrance("Fifty Star and Six Seed Projector"), HasAllCounts({"Power Star": 50, "Cosmic Seed": 6}) & CanReachLocation("Showdown with the Showrunner Defeat The Showrunner"))
    world.set_rule(world.get_entrance("Orchestral Keys Koopa Shell"), Has("Koopa Shell")) #Every single star requires the Koopa Shell. Technically redundant to add because swts requires the Koopa Shell, but it's not a hard requirement.
    world.set_rule(world.get_entrance("Eighteen Star Laser"), Has("Cosmic Seed", count=18))

def set_location_rules(world: 'BTCMWorld'):

    koopa_shell = Has("Koopa Shell")
    rocket_boots = Has("Rocket Boots")
    pandora_boxes = Has("Pandora Boxes")
    vanetal_cap = Has("Vanetal Cap")

    lava_boost_badge = Has("Lava Boost Badge")
    double_time_badge = Has("Double Time Badge")
    greed_badge = Has("Greed Badge")
    squish_badge = Has("Squish Badge")
    feather_badge = Has("Feather Badge")
    sticky_badge = Has("Sticky Badge")
    fast_foot_badge = Has("Fast Foot Badge")

    qfc = CanReachLocation("IR: QUEST FOR CHEESE") #I'm aware that none of these IR levels actually have requirements but uhhh. Preparing for move rando copium.
    gfor = CanReachLocation("IR: GOLD FRIEND ONION RINGS")
    ld = CanReachLocation("IR: LAUNDRY DAY")
    dogfight = CanReachLocation("TT: DOGFIGHT WITH THE WHOMP KING")
    tfe_first_levels = CanReachLocation("TFE: JAGGED WALL KICKS TO THE TOP") & CanReachLocation("TFE: PINK COINS AROUND THE PARK") & CanReachLocation("TFE: HIGHCANE HEIST")
    tfe_blackstone = CanReachLocation("TFE: SCALE THE BLACKSTONE MOUNTAIN")
    tfe_ttt = CanReachLocation("TFE: THROUGH THE TALL TALL TOWERS")
    tfe_100c = CanReachLocation("TFE: EMPIRE'S WEALTH")

    world.set_rule(world.get_location("RHR: CLIMB UP THE LAVAFALL"), lava_boost_badge) #Not that hard w/out it but you're clearly supposed to use it. Will make an option to turn this off.
    world.set_rule(world.get_location("RHR: TIMED RING CHALLENGE"), koopa_shell)
    world.set_rule(world.get_location("RHR: KING BULLY BATTLE"), pandora_boxes)
    world.set_rule(world.get_location("LFF: REMATCH WITH THE HOG"), pandora_boxes) #Let the record show I spent like idk 30 minutes trying to see if "Put the Pig to Sleep" was a prerequisite for this.
    world.set_rule(world.get_location("JS: FRANTIC ROCKET RINGS"), rocket_boots)
    world.set_rule(world.get_location("JS: THE DEATH POKEY"), rocket_boots & pandora_boxes)
    world.set_rule(world.get_location("TPS: NAVAL WARFARE"), pandora_boxes)
    world.set_rule(world.get_location("VP: THE EXECUTIVE"), pandora_boxes)
    world.set_rule(world.get_location("CC: THE GREAT TRAIN ROBBERY"), pandora_boxes)
    world.set_rule(world.get_location("IR: GOLD FRIEND ONION RINGS"), qfc)
    world.set_rule(world.get_location("IR: LAUNDRY DAY"), qfc)
    world.set_rule(world.get_location("IR: FIRE!"), gfor & ld) #Don't need to check for Quest for Cheese because the previous 2 levels already require it.
    world.set_rule(world.get_location("IR: GIANT'S LOOSE CHANGE"), qfc | greed_badge) #Probably not possible to get 100 coins w/out greed. Feel free to prove me wrong.
    world.set_rule(world.get_location("IR: VACUUM CHASE"), pandora_boxes) #This is the point where I realized it's spelled "VACCUM CHASE" in-game but I'm not changing it rn.
    world.set_rule(world.get_location("IR: Costume in the kitchen sink"), qfc)
    world.set_rule(world.get_location("RL: SHELL SURFING AND THWOMP RIDING"), koopa_shell)
    world.set_rule(world.get_location("TT: RINGS UPON THE TOWER PEAKS"), rocket_boots)
    world.set_rule(world.get_location("TT: SHELL RIDE UP THE LAVA FOUNTAIN"), koopa_shell)
    world.set_rule(world.get_location("TT: DOGFIGHT WITH THE WHOMP KING"), rocket_boots)
    #world.set_rule(world.get_location("TT: SNAKE BLOCK MUTINY"), sticky_badge) Keeping this as a reminder for when I add options
    world.set_rule(world.get_location("BB: POWER OF VANETAL"), vanetal_cap)
    world.set_rule(world.get_location("BB: THE 5000 IQ SUPERQUIZ"), pandora_boxes & dogfight)
    world.set_rule(world.get_location("BB: Costume in the quiz area"), pandora_boxes & dogfight) #Was gonna make this require reaching the Superquiz, but technicalyyyyy you don't need to reach it, you just need to get pandora boxes and dogfight
    world.set_rule(world.get_location("SiSt: THE STAR POWER PLANT"), squish_badge) #Doing this one because there's a huge squish point near the end and it's kinda frustrating from my testing.
    world.set_rule(world.get_location("SiSt: Costume at the end of the star factory"), squish_badge)
    world.set_rule(world.get_location("OK: SHELL SHREDDIN' THE SUNKEN ROOVES"), double_time_badge) #When I first played this hack this star was nearly impossible for me without this. May be a skill issue idk.
    world.set_rule(world.get_location("HuHa: PINK COINS ON THE SLOPES"), vanetal_cap)
    world.set_rule(world.get_location("HuHa: RING GRAFFITI"), vanetal_cap)
    world.set_rule(world.get_location("TFE: SCALE THE BLACKSTONE MOUNTAIN"), tfe_first_levels & feather_badge & sticky_badge) #Pretty frustrating level if you don't have these imo.
    world.set_rule(world.get_location("TFE: THROUGH THE TALL TALL TOWERS"), tfe_blackstone)
    world.set_rule(world.get_location("TFE: TEMPLE GUARDIAN"), tfe_ttt & tfe_100c)
    world.set_rule(world.get_location("ToT: RED TRIAL"), koopa_shell)
    world.set_rule(world.get_location("ToT: GREEN TRIAL"), vanetal_cap)
    world.set_rule(world.get_location("ToT: HEART OF AGAMEMNON"), rocket_boots)
    world.set_completion_rule(CanReachLocation("ToT: HEART OF AGAMEMNON"))










