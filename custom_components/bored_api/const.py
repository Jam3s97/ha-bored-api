"""Constants for the Bored API integration."""

import logging
from datetime import timedelta

DOMAIN = "bored_api"
LOGGER = logging.getLogger(__package__)

API_URL = "https://bored-api.appbrewery.com/random"
UPDATE_INTERVAL = timedelta(hours=1)
