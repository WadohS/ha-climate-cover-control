# ha-climate-cover-control

Français | [English](README.md)

Blueprint Home Assistant **Climate Cover Control** pour la gestion des volets par façade, avec prise en compte du soleil, de la chaleur, des jours travaillés, des vacances et d’une fermeture saisonnière.

Ce blueprint est prévu pour les maisons où chaque façade reçoit le soleil à des moments différents et où les volets ne doivent pas tous réagir de la même manière.

[![Ouvrir Home Assistant et importer le blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/WadohS/ha-climate-cover-control/main/blueprints/automation/climate_cover_control_fr.yaml)

## Blueprints et intégration

- **Blueprints** : version fonctionnelle recommandée aujourd’hui. Import FR : [climate_cover_control_fr.yaml](https://raw.githubusercontent.com/WadohS/ha-climate-cover-control/main/blueprints/automation/climate_cover_control_fr.yaml), import EN : [climate_cover_control_en.yaml](https://raw.githubusercontent.com/WadohS/ha-climate-cover-control/main/blueprints/automation/climate_cover_control_en.yaml).
- **Intégration custom** : préparation pour une évolution future avec groupes de contrôle, azimut par groupe, horaires indépendants et phases avant/pendant/après fenêtre solaire. Voir [documentation intégration](docs/integration.fr.md).
- Les deux approches sont prévues pour pouvoir cohabiter pendant une transition, à condition de ne pas piloter le même volet avec les deux en même temps.

## Fonctionnalités

- Pilotage de plusieurs volets pour une même façade/exposition.
- Action d’ouverture du matin configurable lors des journées chaudes : garder fermé, ouvrir partiellement, ou ouvrir complètement.
- Réouverture quand le soleil ne tape plus sur la façade.
- Fenêtre solaire intégrée optionnelle basée sur l’azimut/élévation de `sun.sun`, pour éviter de dépendre obligatoirement d’un binary sensor soleil direct.
- Réouverture complète ou partielle configurable.
- Horaires d’ouverture par jour de la semaine.
- Capteurs optionnels : jour travaillé, jour férié, vacances, absence/sécurité.
- Fermeture au coucher du soleil avec offsets mensuels configurables.
- Fonctionne localement dans Home Assistant.

## Principe

Journée normale :

```text
ouverture à l’heure configurée, avec respect du lever du soleil si activé
fermeture au coucher du soleil + offset mensuel
```

Journée chaude :

```text
les volets restent fermés le matin, ou s’ouvrent partiellement/complètement selon le réglage
ils peuvent rouvrir lorsque le soleil ne tape plus sur la façade
la réouverture peut être partielle ou complète
fermeture au coucher du soleil + offset mensuel
```

## Importer dans Home Assistant

URL d’import manuel :

```text
https://raw.githubusercontent.com/WadohS/ha-climate-cover-control/main/blueprints/automation/climate_cover_control_fr.yaml
```

Il est aussi possible de copier manuellement le fichier blueprint voulu dans Home Assistant :

```text
/config/blueprints/automation/climate_cover_control_fr.yaml
```

Puis créer une automatisation à partir du blueprint dans Home Assistant.

## Test recommandé

Commencer avec une seule façade, par exemple cuisine / salle à manger :

```text
cover.volet_cuisine
cover.volet_salle_a_manger
```

Avec soit un capteur soleil direct de façade, par exemple :

```text
binary_sensor.facade_est_sud_sun_direct
```

soit la fenêtre solaire intégrée. Exemple pour une façade Sud-Est dont la perpendiculaire du mur est à 145° :

```yaml
sun_detection_mode: solar_window
facade_azimuth: 145
solar_window_before: 65   # 145 - 65 = début de fenêtre à 80°
solar_window_after: 75    # 145 + 75 = fin de fenêtre à 220°
solar_elevation_min: 3
```

Pendant les tests, désactiver les autres automatisations qui pilotent les mêmes volets pour éviter les conflits.

## Statut

Version actuelle : `0.1.3`

Version initiale. À tester sur un petit groupe de volets avant généralisation.

## Documentation

- [Intégration custom — préparation / conception](docs/integration.fr.md)
- [Guide de configuration — Français](docs/configuration.fr.md)
- [Feuille de route / idées — Français](docs/roadmap.fr.md)
- [Custom integration — preparation / design](docs/integration.en.md)
- [Configuration guide — English](docs/configuration.en.md)
- [Roadmap / ideas — English](docs/roadmap.en.md)

## Licence

MIT
