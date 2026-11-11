"""Buttons for the Bored API integration."""

from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.components.button import ButtonEntity

from .entity import BoredApiEntity

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

    from .coordinator import BoredApiCoordinator
    from .data import BoredApiConfigEntry


async def async_setup_entry(
    hass: HomeAssistant,  # noqa: ARG001
    entry: BoredApiConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up buttons."""
    async_add_entities([BoredApiNewActivityButton(entry.runtime_data)])


class BoredApiNewActivityButton(BoredApiEntity, ButtonEntity):
    """Button that fetches a new random activity."""

    def __init__(self, coordinator: BoredApiCoordinator) -> None:
        """Initialize the button."""
        super().__init__(coordinator, "new_activity")

    async def async_press(self) -> None:
        """Fetch a new activity."""
        await self.coordinator.async_request_refresh()
