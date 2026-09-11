from typing import Tuple

#A tuple of items where they share the same index as the id of the respective items
btcm_items: Tuple[str, ...] = (
    "Power Star",
    "Cosmic Seed",
    "Blue Star",
    "Lens",
    "Starfair Key",
    "Rocket Boots",
    "Pandora Boxes",
    "Vanetal Cap",
    "Koopa Shell",
    "Wallet",
    "Lava Boost Badge",
    "Fall Damage Badge",
    "Defense Badge",
    "Double Damage Badge",
    "Gills Badge",
    "Fins Badge",
    "HP Regen Badge",
    "Mana Regen Badge",
    "Greed Badge",
    "Double Time Badge",
    "Magnet Badge",
    "Star Radar Badge",
    "Burn Badge",
    "Squish Badge",
    "Feather Badge",
    "Weight Badge",
    "Sticky Badge",
    "Fast Foot Badge",
    "Heal Plus Badge",
    "Bottomless Badge",
    "Boss Slayer Badge",
    "Brittle Burden",
    "Withering Burden",
    "Save Shatter Burden",
)

#Here in case I wanna add the "What item you're going to get if you buy this" indicator some AP's have.
#DO NOT FUCKING ADD THIS BEFORE 1.0
char_to_hex = {
    "0" : 0x0, "1" : 0x1, "2" : 0x2, "3" : 0x3, "4" : 0x4, "5" : 0x5,
    "6" : 0x6, "7" : 0x7, "8" : 0x8, "9" : 0x9, "A" : 0xA, "B" : 0xB,
    "C" : 0xC, "D" : 0xD, "E" : 0xE, "F" : 0xF, "G" : 0x10, "H" : 0x11,
    "I" : 0x12, "J" : 0x13, "K" : 0x14, "L" : 0x15, "M" : 0x16,
    "N" : 0x17, "O" : 0x18,"P" : 0x19, "Q" : 0x1A, "R" : 0x1B,
    "S" : 0x1C, "T" : 0x1D, "U" : 0x1E, "V" : 0x1F, "W" : 0x20,
    "X" : 0x21, "Y" : 0x22, "Z" : 0x23, "a" : 0x24, "b" : 0x25,
    "c" : 0x26, "d" : 0x27, "e" : 0x28, "f" : 0x29, "g" : 0x2A,
    "h" : 0x2B, "i" : 0x2C, "j" : 0x2D, "k" : 0x2E, "l" : 0x2F,
    "m" : 0x30, "n" : 0x31, "o" : 0x32, "p" : 0x33, "q" : 0x34,
    "r" : 0x35, "s" : 0x36, "t" : 0x37, "u" : 0x38, "v" : 0x39,
    "w" : 0x3A, "x" : 0x3B, "y" : 0x3C,"z" : 0x3D, " " : 0x9E
}