import asyncio


class WebsocketService:
    """Handles websocket connections."""

    async def start(self):
        while True:
            await asyncio.sleep(1)
            # TODO: implement websocket logic
