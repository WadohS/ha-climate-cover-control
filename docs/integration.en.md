# Home Assistant integration — Climate Cover Control

Status: **preparation / design**.

The blueprint remains the functional version to use for now. The custom integration is prepared in the repository so a gradual migration can happen later, while still allowing coexistence with the blueprints.

## Goal

The integration should manage cover groups by facade/exposure logic with a more structured configuration than multiple separate blueprint automations.

Important principles:

- a control group is independent from a Home Assistant room/area;
- the same room may have multiple exposures;
- multiple groups may share the same azimuth while keeping different schedules;
- Home Assistant areas and labels may help select covers, but must not decide the solar logic on their own;
- the integration should coexist with the blueprints as long as the same cover is not controlled by both at the same time.

## Target model

### Control group

Each group should carry its own configuration:

```yaml
name: Kitchen South-East
covers:
  - cover.volet_cuisine
  - cover.volet_salle_a_manger
azimuth: 145
solar_window_before: 65
solar_window_after: 75
solar_elevation_min: 3
```

Azimuth is a group property, not the unique group identifier. Two groups can therefore share the same azimuth:

```text
Kitchen South-East — azimuth 145° — opening 07:30
Living room South-East — azimuth 145° — opening 09:00
```

## Customizable phases

The integration should keep a clear separation between these phases:

1. morning opening;
2. before solar window;
3. during solar window;
4. after solar window;
5. evening;
6. night.

For each phase, it should be possible to configure:

- action: do nothing, open, close, specific position;
- position percentage when needed;
- weather/heat conditions;
- whether manual actions are respected;
- schedules or triggers.

## Evening / night closing

Night handling should be highly customizable:

- close at sunset with offset;
- close at a fixed time;
- partial close for ventilation;
- full close later;
- separate evening and night phases.

Examples:

```text
Kitchen: sunset + 30 min → 15%, then 23:00 → closed
Bedroom: sunset - 10 min → closed
Living room: 22:30 → closed
```

## Coexistence with blueprints

During the transition:

- the blueprint remains recommended for real use;
- the integration must not control covers until explicitly configured;
- avoid controlling the same cover from both a blueprint and the integration;
- the integration may first provide sensors/debug, then control actions later.

## First technical step

The repository contains a minimal scaffold in:

```text
custom_components/climate_cover_control/
```

It does not create entities yet and does not take control of covers. It is only a base for building the integration later.
