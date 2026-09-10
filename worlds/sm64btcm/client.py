from typing_extensions import TYPE_CHECKING
from worlds._bizhawk.client import BizHawkClient
import worlds._bizhawk as bizhawk
from .data import btcm_items

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

saveFileBufferPtr = 0x89CB0
marioStatePtr = 0x237CF0
courseStarsPtr = saveFileBufferPtr + 0x14
numStarsPtr = saveFileBufferPtr + 0x4F
numMetalStarsPtr = saveFileBufferPtr + 0x53
flagsPtr  = saveFileBufferPtr + 0x10
storyFlagsPtr = saveFileBufferPtr + 0x11
walletsPtr = saveFileBufferPtr + 0x2
archWalletsPtr = saveFileBufferPtr + 0x56
globalCoinsPtr = marioStatePtr + 0x104
maxGlobalCoinsPtr = marioStatePtr + 0x106


def hex_to_int(hex_values:bytes):
    return_value = 0
    for index, value in enumerate(hex_values[::-1]):
        return_value += value * pow(256, index)
    return return_value

class BTCMClient(BizHawkClient):
#Despite the fact this is a "BizHawkClient", this is not meant to use BizHawk
#Use Luna's Project64 with connector_pj64_generic.js
    game = "Super Mario 64: Beyond the Cursed Mirror"
    system = "N64"

    unsentCoins = 0

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        try:
            # Check ROM name/patch version
            rom_name = ((await bizhawk.read(ctx.bizhawk_ctx, [(0x20, 20, "ROM")]))[0]).decode("ascii")
            if rom_name != "SM64 BTCM ARCH      ":
                return False
        except bizhawk.RequestFailedError:
            return False

        ctx.game = self.game
        ctx.items_handling = 0b111
        ctx.want_slot_data = True
        ctx.watcher_timeout = 0.5

        return True

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        try:

            reads = [
                (courseStarsPtr, 25, "RDRAM"), #0
                (flagsPtr, 4, "RDRAM"), #1
                (walletsPtr, 2, "RDRAM"), #2
                (archWalletsPtr, 2, "RDRAM"), #3
                (globalCoinsPtr, 2, "RDRAM"), #4
                (maxGlobalCoinsPtr, 2, "RDRAM"), #5
            ]
            read = await bizhawk.read(ctx.bizhawk_ctx, reads)
            #Check which locations have been checked and send them
            #First up is all of the course stars
            locs_to_send = []
            current_star = 0
            for byte in list(read[0]):
                for index, bit in enumerate(reversed(format(byte,"08b"))):
                    if index >= 7:
                        continue
                    else:
                        current_star += 1
                    if bit == "1":
                        locs_to_send.append(current_star) #Most star locations are indexed at what bit they are stored at in the course stars variable
            #Next Up is the flags (which includes the stars from minigames)
            idx = 1
            for byte in list(read[1]):
                for bit in format(byte,"08b"):
                    if bit == "1":
                        locs_to_send.append(idx + 1000) #All Flag-related locations are indexed at 1000+what bit
                    idx += 1                            #they are stored at in the flags variable
            #Third up, Wallets
            idx = 1
            for byte in list(read[2]):
                for bit in format(byte,"08b"):
                    if bit == "1":
                        locs_to_send.append(idx + 2000) #Same as above but with 2000
                    idx += 1
            await ctx.send_msgs([{"cmd": "LocationChecks","locations": locs_to_send}])
            #Check which items have been received and change the game state accordingly
            writes = []
            power_stars = 0
            cosmic_seeds = 0
            wallets = 1 #You start off with 1 wallet
            flags = [0,0,0,0,0,0,0,0]
            for item in ctx.items_received:
                item_name = btcm_items[item.item-1]
                match item_name:
                    case "Power Star":
                        power_stars += 1
                    case "Cosmic Seed":
                        cosmic_seeds += 1
                    case "Lens":
                        flags[1] = 1
                    case "Starfair key":
                        flags[2] = 1
                    case "Rocket Boots":
                        flags[3] = 1
                    case "Pandora Boxes":
                        flags[4] = 1
                    case "Vanetal Cap":
                        flags[5] = 1
                    case "Koopa Shell":
                        flags[6] = 1
                    case "Wallet":
                        wallets += 1
            if power_stars > 255:
                power_stars = 255
            if cosmic_seeds > 255:
                cosmic_seeds = 255
            if wallets > 16:
                wallets = 16
            flags_write = 0
            for index, value in enumerate(flags):
                flags_write += value * pow(2, index)
            #For wallets we need to do something special since you're supposed to get +50 coins per wallet.
            #Normally I'd just +50 since your coin cap is going to increase anyways, but doing this could
            #lead to coins you're currently collecting getting deleted due to the delay between reading
            #and writing.
            prev_num_of_wallets = format(hex_to_int(read[3]),"016b").count("1")
            if wallets > prev_num_of_wallets:
                #First we write to RDRAM a bit for every wallet we have (this is normal)
                wallet_write = 0
                for i in range(wallets):
                    wallet_write += pow(2,i)
                writes.append((archWalletsPtr, wallet_write.to_bytes(2), "RDRAM"))
                #Then we try to send coins to the player
                self.unsentCoins += 50 * (wallets - prev_num_of_wallets)

            if self.unsentCoins > 0:
                #We might not have actually sent the wallet yet. So we're calculating what the max should be
                max_coins = hex_to_int(read[5]) + (50 * wallets - prev_num_of_wallets)
                coins_to_send = hex_to_int(read[4]) + self.unsentCoins
                #Only needed because sometimes I like to set my coins to the limit manually
                if coins_to_send > 1000:
                    coins_to_send = min(coins_to_send, 65535)
                    max_coins = 65535
                write_result = await bizhawk.guarded_write(
                    ctx.bizhawk_ctx,
                    [(globalCoinsPtr, min(coins_to_send,max_coins).to_bytes(2), "RDRAM")],
                    [(globalCoinsPtr, read[4], "RDRAM")]
                )
                if write_result:
                    #Note that we might not have sent all of the coins to the player. But that's okay.
                    self.unsentCoins = 0



            writes.append((numStarsPtr, power_stars.to_bytes(), "RDRAM"))
            writes.append((numMetalStarsPtr, cosmic_seeds.to_bytes(), "RDRAM"))
            writes.append((storyFlagsPtr, flags_write.to_bytes(), "RDRAM"))
            await bizhawk.write(ctx.bizhawk_ctx, writes)

        except bizhawk.RequestFailedError:
            pass