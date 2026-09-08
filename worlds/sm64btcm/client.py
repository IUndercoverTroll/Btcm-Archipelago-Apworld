from typing_extensions import TYPE_CHECKING
from worlds._bizhawk.client import BizHawkClient
import worlds._bizhawk as bizhawk
from .data import btcm_items

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

saveFileBufferPtr = 0x89CB0
courseStarsPtr = saveFileBufferPtr + 0x14
numStarsPtr = saveFileBufferPtr + 0x53
numMetalStarsPtr = saveFileBufferPtr + 0x57

class BTCMClient(BizHawkClient):
#Despite the fact this is a "BizHawkClient", this is not meant to use BizHawk
#Use Luna's Project64 with connector_pj64_generic.js
    game = "Super Mario 64: Beyond the Cursed Mirror"
    system = "N64"

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        from CommonClient import logger
        try:
            logger.warning("Hi")
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
        from CommonClient import logger
        try:
            reads = [
                (courseStarsPtr, 25, "RDRAM"), #0
            ]
            read = await bizhawk.read(ctx.bizhawk_ctx, reads)
            #Check which locations have been checked and send them
            locs_to_send = []
            current_star = 0
            for byte in list(read[0]):
                for index, bit in enumerate(reversed(bin(byte))):
                    current_star += 1
                    if index >= 7:
                        continue
                    if bit == "1":
                        locs_to_send.append(current_star)
            await ctx.send_msgs([{"cmd": "LocationChecks","locations": locs_to_send}])

            writes = []
            power_stars = 0
            cosmic_seeds = 0
            for item in ctx.items_received:
                item_name = btcm_items[item.item-1]
                match item_name:
                    case "Power Star":
                        power_stars += 1
                    case "Cosmic Seed":
                        cosmic_seeds += 1
            if power_stars > 255:
                power_stars = 255
            if cosmic_seeds > 255:
                cosmic_seeds = 255
            logger.info("Hi")
            logger.info(power_stars)
            writes.append((numStarsPtr, power_stars, "RDRAM"))
            writes.append((numMetalStarsPtr, cosmic_seeds, "RDRAM"))
            await bizhawk.write(ctx.bizhawk_ctx, writes)

        except bizhawk.RequestFailedError:
            pass