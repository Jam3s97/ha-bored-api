# Bored API for Home Assistant

Suggests random activities from <https://bored-api.appbrewery.com/random>.

## Install
1. HACS → ⋮ → Custom repositories → add this repo as *Integration*.
2. Download, restart Home Assistant.
3. Settings → Devices & services → Add integration → **Bored API**.

## Entities
- Sensors: Activity (attributes: kid_friendly, link, availability, key), Type, Participants, Price (%), Accessibility, Duration.
- Button: **New activity** – fetches a new random activity immediately.

The activity is refreshed hourly. No configuration or API key needed.
