"""Climate Cover Control custom integration scaffold.

This package is intentionally minimal for now: the production-ready behavior lives
in the Home Assistant blueprints while the integration design is prepared.
"""

from __future__ import annotations

from homeassistant.core import HomeAssistant

from .const import DOMAIN


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up Climate Cover Control from YAML, if present.

    No entities or services are registered yet. This keeps the future integration
    able to coexist with the blueprint without taking control of any cover.
    """
    hass.data.setdefault(DOMAIN, {})
    return True
