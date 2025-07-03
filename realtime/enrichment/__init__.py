import asyncio


class EnrichmentService:
    """Enriches token information."""

    async def start(self):
        while True:
            await asyncio.sleep(1)
            # TODO: implement enrichment logic
