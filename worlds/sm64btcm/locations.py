from BaseClasses import Location

class BTCMLocation(Location):
    game = "Super Mario 64: Beyond the Cursed Mirror"

RHR_table = {
    "RHR: THE MIMIC STARS": 1,
    "RHR: RED COIN BLAST": 2,
    "RHR: CLIMB UP THE LAVAFALL": 3,
    "RHR: STEEL CRATE CLEANUP": 4,
    "RHR: TIMED RING CHALLENGE": 5,
    "RHR: THE SEARCH FOR 100 COINS": 6,
    "RHR: KING BULLY BATTLE": 7,
    "Red Hot Reservoir Wallet": 2016,
    "Lava Boost Badge (Shop)": 3024,
    "Burn Badge (Shop)": 3012,
}

LFF_table = {
    "LFF: UNEARTH THE PIRANHA WEEDS": 8,
    "LFF: TO THE TOP OF THE BARN": 9,
    "LFF: DOWN THE SILO SLIDE": 10,
    "LFF: PUT THE PIG TO SLEEP": 11,
    "LFF: HORSE RIDIN' RINGS": 12,
    "LFF: FARMER'S LOOSE CHANGE": 13,
    "LFF: REMATCH WITH THE HOG": 14,
    "Lonely Floating Farm Wallet": 2015,
}

JS_table = {
    "JS: THE 5 YOSHI COINS": 15,
    "JS: TOP OF THE MOUNTAIN": 16,
    "JS: FREE THE VILLAGE": 17,
    "JS: SKYWARD SNAKEBLOCK": 18,
    "JS: FRANTIC ROCKET RINGS": 19,
    "JS: 100 PREHISTORIC COINS": 20,
    "JS: THE DEATH POKEY": 21,
    "Jurassic Savanna Wallet": 2014,
}

TPS_table = {
    "TPS: TOP OF THE MAIN MAST": 22,
    "TPS: 8 REDS OF THE LOST SEA": 23,
    "TPS: WALK THE GHOSTLY PLANKS": 24,
    "TPS: SLIPPERY SNAKE BLOCK": 25,
    "TPS: THE GHOST'S GOBLET": 26,
    "TPS: 100 SEA SICK COINS": 27,
    "TPS: NAVAL WARFARE": 28,
    "The Phantom Strider Wallet": 2012, #For some reason TPS skips flag 13 which is instead used for the VP wallet
    "Gills Badge (Shop)": 3020,
    "Fins Badge (Shop)": 3019,
    "Star Radar Badge (Shop)": 3013,
}

VP_table = {
    "VP: LEAPING ACROSS THE ROOFTOPS": 29,
    "VP: DOWN THE SEPTIC SLIDE": 30,
    "VP: CRATES AND BUTTONS": 31,
    "VP: MEDIEVAL COLOSSEUM TRIALS": 32,
    "VP: DIGITAL VORTEX OF DEATH": 33,
    "VP: 100 BYTECOINS": 34,
    "VP: THE EXECUTIVE": 35,
    "Virtuaplex Switch": 1030,
    "Virtuaplex Wallet": 2013,
}

CC_table = {
    "CC: EYE OUT FOR TUMBLING BOULDERS": 36,
    "CC: COASTING BY WITH THE B.BILL MASK": 37,
    "CC: REDS OF THE PROSPECTOR'S CAVE": 38,
    "CC: PROSPECTOR'S HOT ROPE JUMP": 39,
    "CC: BANDIT BEATDOWN": 40,
    "CC: THE COLLECTION OF THE SCRIP": 41,
    "CC: THE GREAT TRAIN ROBBERY": 42,
    "Cowboy Canyon Wallet": 2011,
}

IR_table = {
    "IR: QUEST FOR CHEESE": 43,
    "IR: RED COINS OF THE LIVING ROOM": 44,
    "IR: GOLD FRIEND ONION RINGS": 45,
    "IR: LAUNDRY DAY": 46,
    "IR: FIRE!": 47,
    "IR: GIANT'S LOOSE CHANGE": 48,
    "IR: VACUUM CHASE": 49,
    "Immense Residence Wallet": 2010
}

RL_table = {
    "RL: PIPE DREAM": 50,
    "RL: SCALING THE MUSHROOM MOUNTAIN": 51,
    "RL: SHELL SURFING AND THWOMP RIDING": 52,
    "RL: THE HEAT BELOW THE ICE": 53,
    "RL: PHANTO'S CURSED KEY": 54,
    "RL: 1-UP TIME": 55,
    "RL: BIT SIZED BOWSER": 56,
    "Retroland Wallet": 2009,
}

TT_table = {
    "TT: DUEL THE THWOMP KING": 57,
    "TT: RINGS UPON THE TOWER PEAKS": 58,
    "TT: SHELL RIDE UP THE LAVA FOUNTAIN": 59,
    "TT: DOGFIGHT WITH THE WHOMP KING": 60,
    "TT: SNAKE BLOCK MUTINY": 61,
    "TT: TREASURE OF THE THWOMP KING": 62,
    "TT: ATTACK OF THE THWOMP QUEEN": 63,
    "Thwomp Towers Wallet": 2008,
    "Fast Foot Badge (Shop)": 3007,
    "Sticky Badge (Shop)": 3008,
    "Feather Badge (Shop)": 3010,
}

BB_table = {
    "BB: ATOP THE BUILDING PEAKS": 64,
    "BB: REDS IN THE SERVERS & CITY": 65,
    "BB: HEXAGONS IN THE HOLE": 66,
    "BB: POWER OF VANETAL": 67,
    "BB: TUBING DOWN THE TUNNEL": 68,
    "BB: HAMMER BRO HUNDREDS": 69,
    "BB: THE 5000 IQ SUPERQUIZ": 70,
    "Blueberg Key": 1026,
    "Blueberg Switch": 1029,
    "Blueberg Wallet": 2007,
    "HP Regen Badge (Shop)": 3018,
    "Greed Badge (Shop)": 3016,
    "Double Time Badge (Shop)": 3015,
}

SiSt_table = {
    "SiSt: FERRIS WHEEL FUN": 71,
    "SiSt: THE STAR POWER PLANT": 72,
    "SiSt: RED COINS ON MAIN STREET": 73,
    "SiSt: THE FOUR SISTERS": 74,
    "SiSt: ROOFTOP RINGS": 75,
    "SiSt: EDWARD CONE COINS": 76,
    "SiSt: CAREFULLY CLIMB THE CONSTRUCTION": 77,
    "Sinful Starfair Wallet": 2005,
    "Heal Plus Badge (Shop)": 3006,
    "Bottomless Badge (Shop)": 3005,
    "Boss Slayer Badge (Shop)": 3004,
}

OK_table = {
    "OK: THE CLIFFS OF SAXAPHONE SKERRY": 78,
    "OK: SHELL SHREDDIN' THE SUNKEN ROOVES": 79,
    "OK: SHATTER THE 5 COSMIC ORBS": 80,
    "OK: PINK COINS OF THE ISLES": 81,
    "OK: SECRET PASSAGEWAY TO THE WINDMILL": 82,
    "OK: 100 COINS OF THE SOULS WHO PAID": 83,
    "OK: COSMIC ERUPTION": 84,
}

HuHa_table = {
    "HuHa: TOP OF THE TOWN": 85,
    "HuHa: PINK COINS ON THE SLOPES": 86,
    "HuHa: RING GRAFFITI": 87,
    "HuHa: MEMORIZATION OF THE WOODEN HOUSE": 88,
    "HuHa: COSMIC SEED IN THE CAGE": 89,
    "HuHa: 100 BLOCKY COINS": 90,
    "HuHa: DESTROY THE GOLDEN IDOLS": 91,
}

TFE_table = {
    "TFE: JAGGED WALL KICKS TO THE TOP": 92,
    "TFE: PINK COINS AROUND THE PARK": 93,
    "TFE: HIGHCANE HEIST": 94,
    "TFE: SCALE THE BLACKSTONE MOUNTAIN": 95,
    "TFE: THROUGH THE TALL TALL TOWERS": 96,
    "TFE: EMPIRE'S WEALTH": 97,
    "TFE: TEMPLE GUARDIAN": 98,
}

ToT_table = {
    "ToT: RED TRIAL": 99,
    "ToT: YELLOW TRIAL": 100,
    "ToT: GREEN TRIAL": 101,
    "ToT: CYAN TRIAL": 102,
    "ToT: BLUE TRIAL": 103,
    "ToT: PINK TRIAL": 104,
    "ToT: HEART OF AGAMEMNON": 105,
}

BotH_table = {
    "Bowser on the Highway Red Coins": 106,
    "Bowser on the Highway Defeat UrBowser": 107,
    "Bowser on the Highway Pandora Box": 112,
    "Bowser on the Highway Lens": 1027,
}

SwtS_table = {
    "Showdown with the Showrunner Red Coins": 113,
    "Showdown with the Showrunner Defeat The Showrunner": 119,
}

SSS_table = {
    "Sloppy Shell Sewers Red Coins": 127,
    "Sloppy Shell Sewers Switch": 1028,
}

LS_table = {
    "Lost City Red Coins": 155,
    "Lost City Switch": 1031,
}

Minigame_table = {
    "Arena Survival": 1008,
    "Hot Rope Jump": 1007,
    "Hexagon Heat": 1006,
    "Snakio": 1005,
    "Edward Survival": 1004,
    "Bad Apple Dodge": 1003,
    "Flappy Mario": 1002,
    "Sign Game": 1001,
}

Starting_room_badge_table = {
    "Fall Damage Badge (Shop)": 3023,
    "Defense Badge (Shop)": 3022,
    "Magnet Badge (Shop)": 3014,
    "Brittle Burden (Shop)": 3003,
    "Withering Burden (Shop)": 3002,
    "Save Shatter Burden (Shop)": 3001,
}

Three_seed_room_badge_table = {
    "Squish Badge (Shop)": 3011,
    "Weight Badge (Shop)": 3009,
}

Observatory_badge_table = {
    "Double Damage Badge (Shop)": 3021,
    "Mana Regen Badge (Shop)": 3017,
}

location_table = {**RHR_table,**LFF_table,**JS_table,**TPS_table,**VP_table,
                  **CC_table,**IR_table,**RL_table,**TT_table,**BB_table,
                  **SiSt_table,**OK_table,**HuHa_table,**TFE_table,**ToT_table,
                  **BotH_table,**SwtS_table,**SSS_table,**LS_table,**Minigame_table,
                  **Starting_room_badge_table,**Three_seed_room_badge_table,**Observatory_badge_table}