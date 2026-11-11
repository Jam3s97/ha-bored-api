"""The Bored API integration."""

from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.const import Platform
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .api import BoredApiClient
from .coordinator import BoredApiCoordinator

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant

    from .data import BoredApiConfigEntry

PLATFORMS: list[Platform] = [Platform.BUTTON, Platform.SENSOR]


async def async_setup_entry(hass: HomeAssistant, entry: BoredApiConfigEntry) -> bool:
    """Set up Bored API from a config entry."""
    client = BoredApiClient(async_get_clientsession(hass))
    coordinator = BoredApiCoordinator(hass, client)
    await coordinator.async_config_entry_first_refresh()
    entry.runtime_data = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: BoredApiConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
