"""Data update coordinator for the Bored API integration."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import BoredApiClient, BoredApiError
from .const import DOMAIN, LOGGER, UPDATE_INTERVAL

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant


class BoredApiCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """Fetch a random activity on a schedule or on demand."""

    def __init__(self, hass: HomeAssistant, client: BoredApiClient) -> None:
        """Initialize the coordinator."""
        super().__init__(
            hass,
            LOGGER,
            name=DOMAIN,
            update_interval=UPDATE_INTERVAL,
        )
        self.client = client

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch new activity."""
        try:
            return await self.client.async_get_random_activity()
        except BoredApiError as err:
            raise UpdateFailed(str(err)) from err
