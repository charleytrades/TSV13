import asyncio


class SignalService:
    """Generates trading signals."""

    async def start(self):
        while True:
            await asyncio.sleep(1)
            # TODO: implement signal generation
