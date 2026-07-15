# Intégration Home Assistant — Climate Cover Control

Statut : **préparation / conception**.

Le blueprint reste la version fonctionnelle à utiliser pour le moment. L’intégration custom est préparée dans le dépôt pour permettre une migration progressive plus tard, sans empêcher la cohabitation avec les blueprints.

## Objectif

L’intégration devra permettre de gérer des groupes de volets par logique de façade/exposition, avec une configuration plus structurée que plusieurs automatisations blueprint séparées.

Principes importants :

- un groupe de contrôle est indépendant d’une pièce Home Assistant ;
- une même pièce pourra avoir plusieurs expositions ;
- plusieurs groupes pourront partager le même azimut mais avoir des horaires différents ;
- les zones et labels Home Assistant pourront aider à sélectionner les volets, mais ne devront pas décider seuls de la logique solaire ;
- l’intégration devra pouvoir cohabiter avec les blueprints tant qu’un même volet n’est pas piloté par les deux en même temps.

## Modèle cible

### Groupe de contrôle

Chaque groupe devrait porter sa propre configuration :

```yaml
name: Cuisine Sud-Est
covers:
  - cover.volet_cuisine
  - cover.volet_salle_a_manger
azimuth: 145
solar_window_before: 65
solar_window_after: 75
solar_elevation_min: 3
```

L’azimut est une propriété du groupe, pas son identifiant unique. Deux groupes peuvent donc avoir le même azimut :

```text
Cuisine Sud-Est — azimut 145° — ouverture 07:30
Salon Sud-Est — azimut 145° — ouverture 09:00
```

## Phases à personnaliser

L’intégration devra garder une séparation claire entre les phases suivantes :

1. ouverture du matin ;
2. avant fenêtre solaire ;
3. pendant fenêtre solaire ;
4. après fenêtre solaire ;
5. soirée ;
6. nuit.

Pour chaque phase, on devra pouvoir configurer :

- action : ne rien faire, ouvrir, fermer, position spécifique ;
- position en pourcentage si nécessaire ;
- conditions météo/chaleur ;
- respect ou non des actions manuelles ;
- horaires ou déclencheurs associés.

## Fermeture soir / nuit

La partie nuit devra être très personnalisable :

- fermeture au coucher du soleil avec offset ;
- fermeture à heure fixe ;
- fermeture partielle pour ventilation ;
- fermeture complète plus tard ;
- possibilité de séparer soirée et nuit.

Exemples :

```text
Cuisine : coucher du soleil + 30 min → 15%, puis 23:00 → fermé
Chambre : coucher du soleil - 10 min → fermé
Salon : 22:30 → fermé
```

## Cohabitation avec les blueprints

Pendant la transition :

- le blueprint reste recommandé pour l’usage réel ;
- l’intégration ne doit pas piloter automatiquement les volets tant qu’elle n’est pas explicitement configurée ;
- éviter qu’un même volet soit contrôlé par un blueprint et par l’intégration en même temps ;
- l’intégration pourra d’abord fournir des capteurs/debug, puis des actions de pilotage.

## Première étape technique

Le dépôt contient un squelette minimal dans :

```text
custom_components/climate_cover_control/
```

Il ne crée pas encore d’entité et ne prend pas le contrôle des volets. Il sert uniquement de base pour construire l’intégration plus tard.
