import asyncio


class DiscoveryService:
    """Discovers tokens in real time."""

    async def start(self):
        while True:
            await asyncio.sleep(1)
            # TODO: implement discovery logic
