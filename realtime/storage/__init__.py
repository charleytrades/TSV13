import asyncio


class StorageService:
    """Stores data to SQLite."""

    async def start(self):
        while True:
            await asyncio.sleep(1)
            # TODO: implement storage logic
