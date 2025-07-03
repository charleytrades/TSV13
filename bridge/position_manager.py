import asyncio


class PositionManager:
    """Manages open positions."""

    async def start(self):
        while True:
            await asyncio.sleep(1)
            # TODO: implement position management
