[![oc-project-shield][oc-project-shield]][oc-project-url]

[oc-project-shield]: https://img.shields.io/badge/OPENCLASSROOMS-PROJECT-blueviolet?style=for-the-badge
[oc-project-url]: https://openclassrooms.com/fr/paths/518-developpeur-dapplication-python

# Openclassrooms - Développeur d'application Python - Projet 12

Développez une architecture back-end sécurisée avec Python et SQL

![Epic Events](https://user.oc-static.com/upload/2023/07/26/16903799358611_P12-02.png)

## Compétences évaluées

- :bulb: Mettre en œuvre une base de données sécurisée avec Python et SQL

## Installation et exécution du projet

### Pré-requis

- Avoir `Python`, `pip`, `Poetry` et `postgreSQL` installé sur sa machine.

### Création de la base de données

1. Se connecter à PostgreSQL

```sh
psql -U nom_utilisateur -h adresse_ip -p port
```

2. Créer une base de données PostgreSQL

```sh
CREATE DATABASE nom_de_la_base_de_donnees;
```

3. Créer un utilisateur et lui donner les droits sur la base de données

```sh
CREATE USER nom_utilisateur WITH PASSWORD 'mot_de_passe';
GRANT ALL PRIVILEGES ON DATABASE nom_de_la_base_de_donnees TO nom_utilisateur;
```

4. Créer un fichier `.env` à la racine du projet et ajouter les variables suivantes

```sh
DB_NAME=nom_de_la_base_de_donnees
DB_USER=nom_utilisateur
DB_PASSWORD=mot_de_passe
DB_HOST=adresse_ip
DB_PORT=port
```

### Installation et exécution

1. Cloner le repo

```sh
git clone https://github.com/Gregson971/oc-da-python-p12.git
```

2. Se placer dans le dossier oc-da-python-p12

```sh
cd /oc-da-python-p12
```

3. Installer les dépendances

```sh
poetry install
```

4. Activer l'environnement virtuel

```sh
poetry shell
```

6. Exécuter le script

```sh
python main.py
```
