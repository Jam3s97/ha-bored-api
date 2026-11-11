"""Client for the Bored API (https://bored-api.appbrewery.com)."""

from __future__ import annotations

import asyncio
from typing import Any

import aiohttp

from .const import API_URL


class BoredApiError(Exception):
    """Generic API error."""


class BoredApiConnectionError(BoredApiError):
    """Raised when the API cannot be reached."""

    def __init__(self, err: Exception) -> None:
        """Initialize the error."""
        super().__init__(f"Error fetching activity: {err}")


class BoredApiResponseError(BoredApiError):
    """Raised when the API returns an unexpected payload."""

    def __init__(self) -> None:
        """Initialize the error."""
        super().__init__("Unexpected response from API")


class BoredApiClient:
    """Minimal async client for the random activity endpoint."""

    def __init__(self, session: aiohttp.ClientSession) -> None:
        """Initialize the client."""
        self._session = session

    async def async_get_random_activity(self) -> dict[str, Any]:
        """Fetch a random activity."""
        try:
            async with asyncio.timeout(15):
                response = await self._session.get(API_URL)
                response.raise_for_status()
                data = await response.json()
        except (aiohttp.ClientError, TimeoutError, ValueError) as err:
            raise BoredApiConnectionError(err) from err
        if not isinstance(data, dict) or "activity" not in data:
            raise BoredApiResponseError
        return data
