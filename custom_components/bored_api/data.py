"""Custom types for the Bored API integration."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry

from .coordinator import BoredApiCoordinator

type BoredApiConfigEntry = ConfigEntry[BoredApiCoordinator]
