# ha-climate-cover-control

[Français](README.fr.md) | English

Home Assistant blueprint for **Climate Cover Control**: sun-aware and heat-aware facade cover/shutter automation.

This blueprint manages covers/shutters by facade or exposure. It is designed for homes where each facade receives sun at different times and where covers should behave differently during hot days.

[![Open your Home Assistant instance and import the blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/WadohS/ha-climate-cover-control/main/blueprints/automation/climate_cover_control_en.yaml)

## Blueprints and integration

- **Blueprints**: current functional and recommended version. Import EN: [climate_cover_control_en.yaml](https://raw.githubusercontent.com/WadohS/ha-climate-cover-control/main/blueprints/automation/climate_cover_control_en.yaml), import FR: [climate_cover_control_fr.yaml](https://raw.githubusercontent.com/WadohS/ha-climate-cover-control/main/blueprints/automation/climate_cover_control_fr.yaml).
- **Custom integration**: prepared for a future evolution with control groups, per-group azimuth, independent schedules, and before/during/after solar-window phases. See [integration documentation](docs/integration.en.md).
- Both approaches are intended to coexist during a transition, as long as the same cover is not controlled by both at the same time.

## Features

- Control multiple covers as one facade group.
- Configurable morning action on hot days: keep closed, open partially, or open fully.
- Reopen after the sun no longer hits the facade.
- Optional integrated solar window using `sun.sun` azimuth/elevation, so a separate direct-sun binary sensor is not required.
- Optional partial reopening after a hot day sun block.
- Per-day opening times.
- Optional workday, holiday, vacation, and absence/security sensors.
- Evening closing based on sunset with configurable monthly offsets.
- Local Home Assistant automation; no cloud dependency besides your configured weather provider.

## Basic idea

Normal day:

```text
open at the configured time, respecting sunrise if enabled
close at sunset + monthly offset
```

Hot day:

```text
keep covers closed in the morning, or open partially/fully depending on configuration
wait until the facade is no longer in direct sun
then reopen partially or fully depending on configuration
close at sunset + monthly offset
```

## Import into Home Assistant

Manual import URL:

```text
https://raw.githubusercontent.com/WadohS/ha-climate-cover-control/main/blueprints/automation/climate_cover_control_en.yaml
```

You can also copy the blueprint file manually to:

```text
/config/blueprints/automation/climate_cover_control_en.yaml
```

Then create a new automation from the blueprint in Home Assistant.

## Recommended first test

Start with one facade only, for example kitchen/dining room:

```text
cover.volet_cuisine
cover.volet_salle_a_manger
```

Use either a facade direct-sun binary sensor such as:

```text
binary_sensor.facade_est_sud_sun_direct
```

or use the integrated solar window. Example for a South-East facade whose perpendicular wall direction is 145°:

```yaml
sun_detection_mode: solar_window
facade_azimuth: 145
solar_window_before: 65   # 145 - 65 = 80° window start
solar_window_after: 75    # 145 + 75 = 220° window end
solar_elevation_min: 3
```

Disable any other automation controlling the same covers during the test to avoid conflicts.

## Status

Current version: `0.1.3`

This is an early version. Test on a limited set of covers before deploying widely.

## Documentation

- [Custom integration — preparation / design](docs/integration.en.md)
- [Configuration guide — English](docs/configuration.en.md)
- [Roadmap / ideas — English](docs/roadmap.en.md)
- [Intégration custom — préparation / conception](docs/integration.fr.md)
- [Guide de configuration — Français](docs/configuration.fr.md)
- [Feuille de route / idées — Français](docs/roadmap.fr.md)

## License

MIT
