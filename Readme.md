# Première application en ligne de commande

## Description

Cette application vise à simplifier la recherche et la gestion de fichiers selon leur extension dans un répertoire donné, y compris de manière récursive dans tous les sous-répertoires. Avec la commande `run`, l'utilisateur peut lister les fichiers d'une extension spécifique dans un répertoire ciblé et, si désiré, supprimer ces fichiers en utilisant l'option `--delete`. Pour des opérations dans le répertoire courant, les commandes `search` et `delete` permettent respectivement de rechercher et de supprimer des fichiers d'une certaine extension, simplifiant ainsi la gestion de fichiers.

## Installation

Aucune installation préalable n'est requise à part le téléchargement de l'exécutable `program.exe`, généré via `auto-py-to-exe`.

## Utilisation

### Commande `run`

```
./app.exe run [EXTENSION] [--delete]
```

- `[EXTENSION]` : L'extension des fichiers à chercher. Obligatoire.
- `--delete` : Supprime les fichiers de l'extension spécifiée.

### Commande `search`

```
./app.exe search [EXTENSION]
```

- `[EXTENSION]` : L'extension des fichiers à chercher dans le répertoire courant.

### Commande `delete`

```
./app.exe delete [EXTENSION]
```

- `[EXTENSION]` : L'extension des fichiers à supprimer dans le répertoire courant.

## Exemples

Lister les fichiers `.txt` dans le répertoire courant et ses sous-répertoires :

```
./app.exe run txt
```

Supprimer tous les fichiers `.log` dans le répertoire courant et ses sous-répertoires :

```
./app.exe run log --delete
```

## Contribution

Toute contribution à ce projet est bienvenue. N'hésitez pas à fork le projet, à apporter vos modifications, et à soumettre une pull request.

## Licence

Développé par Nour Amellouk. Ce logiciel est libre de droits et peut être utilisé par quiconque souhaite l'utiliser, sans aucune restriction.
