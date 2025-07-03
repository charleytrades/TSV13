import asyncio

from realtime.discovery import DiscoveryService
from realtime.enrichment import EnrichmentService
from realtime.storage import StorageService
from realtime.signals import SignalService
from realtime.websocket import WebsocketService
from realtime.integrations import IntegrationService
from realtime.monitoring import MonitoringService
from bridge.trading import TradingService
from bridge.position_manager import PositionManager


async def main():
    """Initialize and run all services."""
    discovery = DiscoveryService()
    enrichment = EnrichmentService()
    storage = StorageService()
    signals = SignalService()
    websocket = WebsocketService()
    integrations = IntegrationService()
    monitoring = MonitoringService()
    trading = TradingService()
    positions = PositionManager()

    services = [
        discovery,
        enrichment,
        storage,
        signals,
        websocket,
        integrations,
        monitoring,
        trading,
        positions,
    ]

    await asyncio.gather(*(svc.start() for svc in services))


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
