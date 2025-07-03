import asyncio


class IntegrationService:
    """Integrates with external systems."""

    async def start(self):
        while True:
            await asyncio.sleep(1)
            # TODO: implement integrations
