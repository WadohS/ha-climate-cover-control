# ha-climate-cover-control

<p align="center">
  <strong>Climate Cover Control</strong><br>
  Home Assistant blueprint for sun-aware and heat-aware cover/shutter automation.
</p>

<p align="center">
  <a href="README.en.md">🇬🇧 English</a> ·
  <a href="README.fr.md">🇫🇷 Français</a>
</p>

---

## Choose your language / Choisir la langue

The Home Assistant blueprint UI language depends on the YAML file you import. Pick the file matching your preferred interface language.

La langue de l’interface du blueprint dans Home Assistant dépend du fichier YAML importé. Choisissez le fichier correspondant à votre langue.

| Language / Langue | Documentation | Blueprint file | Import |
|---|---|---|---|
| 🇬🇧 English | [README.en.md](README.en.md) | `blueprints/automation/climate_cover_control_en.yaml` | [![Import English blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/WadohS/ha-climate-cover-control/main/blueprints/automation/climate_cover_control_en.yaml) |
| 🇫🇷 Français | [README.fr.md](README.fr.md) | `blueprints/automation/climate_cover_control_fr.yaml` | [![Importer le blueprint français](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/WadohS/ha-climate-cover-control/main/blueprints/automation/climate_cover_control_fr.yaml) |

## Repository name

This repository is now named **ha-climate-cover-control** and the blueprint is **Climate Cover Control**.

## What it does

- Controls several covers/shutters as one facade/exposure group.
- Blocks morning opening on hot days based on the daily forecast maximum temperature.
- Reopens after the sun no longer hits the facade.
- Can use either a direct-sun binary sensor or an integrated solar window based on `sun.sun` azimuth/elevation.
- Supports workday, holiday, vacation, absence/security sensors, partial reopening and monthly sunset close offsets.

## Documentation

- 🇬🇧 [English documentation](README.en.md)
- 🇫🇷 [Documentation française](README.fr.md)
- 🇬🇧 [Configuration guide](docs/configuration.en.md)
- 🇫🇷 [Guide de configuration](docs/configuration.fr.md)

## License

MIT
