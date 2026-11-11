"""Sensors for the Bored API integration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.const import PERCENTAGE

from .entity import BoredApiEntity

if TYPE_CHECKING:
    from collections.abc import Callable

    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

    from .coordinator import BoredApiCoordinator
    from .data import BoredApiConfigEntry


@dataclass(frozen=True, kw_only=True)
class BoredApiSensorDescription(SensorEntityDescription):
    """Describe a Bored API sensor."""

    value_fn: Callable[[dict[str, Any]], Any]


SENSORS: tuple[BoredApiSensorDescription, ...] = (
    BoredApiSensorDescription(
        key="activity",
        translation_key="activity",
        value_fn=lambda d: d.get("activity"),
    ),
    BoredApiSensorDescription(
        key="type",
        translation_key="type",
        value_fn=lambda d: d.get("type"),
    ),
    BoredApiSensorDescription(
        key="participants",
        translation_key="participants",
        value_fn=lambda d: d.get("participants"),
    ),
    BoredApiSensorDescription(
        key="price",
        translation_key="price",
        native_unit_of_measurement=PERCENTAGE,
        value_fn=lambda d: round(d["price"] * 100) if "price" in d else None,
    ),
    BoredApiSensorDescription(
        key="accessibility",
        translation_key="accessibility",
        value_fn=lambda d: d.get("accessibility"),
    ),
    BoredApiSensorDescription(
        key="duration",
        translation_key="duration",
        value_fn=lambda d: d.get("duration"),
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,  # noqa: ARG001
    entry: BoredApiConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up sensors."""
    async_add_entities(
        BoredApiSensor(entry.runtime_data, description) for description in SENSORS
    )


class BoredApiSensor(BoredApiEntity, SensorEntity):
    """A Bored API sensor."""

    entity_description: BoredApiSensorDescription

    def __init__(
        self, coordinator: BoredApiCoordinator, description: BoredApiSensorDescription
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator, description.key)
        self.entity_description = description

    @property
    def native_value(self) -> Any:
        """Return the sensor value."""
        return self.entity_description.value_fn(self.coordinator.data)

    @property
    def extra_state_attributes(self) -> dict[str, Any] | None:
        """Add extra details to the activity sensor."""
        if self.entity_description.key != "activity":
            return None
        data = self.coordinator.data
        return {
            "kid_friendly": data.get("kidFriendly"),
            "link": data.get("link") or None,
            "availability": data.get("availability"),
            "key": data.get("key"),
        }
