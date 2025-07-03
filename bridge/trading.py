import asyncio


class TradingService:
    """Executes trading strategies."""

    async def start(self):
        while True:
            await asyncio.sleep(1)
            # TODO: implement trading strategies
