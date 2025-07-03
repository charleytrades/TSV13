import asyncio


class MonitoringService:
    """Performs health checks and watchdogs."""

    async def start(self):
        while True:
            await asyncio.sleep(1)
            # TODO: implement health checks and watchdogs
