"""Config flow for the Bored API integration."""

from __future__ import annotations

from typing import Any

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .api import BoredApiClient, BoredApiError
from .const import DOMAIN


class BoredApiConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Bored API."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()

        errors: dict[str, str] = {}
        if user_input is not None:
            client = BoredApiClient(async_get_clientsession(self.hass))
            try:
                await client.async_get_random_activity()
            except BoredApiError:
                errors["base"] = "cannot_connect"
            else:
                return self.async_create_entry(title="Bored API", data={})

        return self.async_show_form(step_id="user", errors=errors)
