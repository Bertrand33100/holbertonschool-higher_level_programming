# Python - Server-Side Rendering

## Description

Ce projet Holberton School permet de découvrir le **Server-Side Rendering (SSR)**, une technique qui consiste à générer des pages HTML côté serveur avant de les envoyer au navigateur.

À travers Python, Flask et le moteur de templates Jinja, l'objectif est d'apprendre à créer des pages web dynamiques à partir de données provenant de différentes sources.

## Objectifs d'apprentissage

À la fin de ce projet, je dois être capable de :

- Comprendre le fonctionnement du rendu côté serveur (SSR).
- Différencier le rendu côté serveur du rendu côté client.
- Utiliser Flask pour créer une application web.
- Créer des modèles HTML dynamiques avec Jinja.
- Utiliser des variables, des boucles et des conditions dans les templates.
- Lire et afficher des données provenant de fichiers JSON et CSV.
- Récupérer des données depuis une base de données SQLite.
- Manipuler des fichiers en Python.
- Vérifier les données reçues et gérer les erreurs.
- Générer du contenu dynamique à partir de données Python.

## Technologies utilisées

- **Python** : traitement des données et logique de l'application.
- **Flask** : framework Python pour créer des applications web.
- **Jinja** : moteur de templates permettant de générer du HTML dynamique.
- **HTML** : structure des pages web.
- **JSON** : format de stockage et d'échange de données.
- **CSV** : format de fichiers contenant des données tabulaires.
- **SQLite** : système de base de données relationnelle.

## Les tâches du projet

### Task 0 - Creating a Simple Templating Program

Créer une fonction Python nommée `generate_invitations` qui génère des invitations personnalisées à partir d'un modèle et d'une liste de participants.

Notions étudiées :

- Fonctions Python.
- Chaînes de caractères et remplacement de texte.
- Listes et dictionnaires.
- Lecture et écriture de fichiers.
- Validation des types et des données.
- Gestion des valeurs manquantes.
- Gestion des erreurs.

### Task 1 - Creating a Basic HTML Template in Flask

Créer une première page HTML à l'aide de Flask et apprendre à utiliser les templates.

Notions étudiées :

- Application Flask.
- Routes.
- Templates HTML.
- Fonction `render_template()`.

### Task 2 - Creating a Dynamic Template with Loops and Conditions in Flask

Afficher des données dynamiques dans une page HTML à l'aide des fonctionnalités de Jinja.

Notions étudiées :

- Variables dans les templates.
- Boucles `for`.
- Conditions `if`.
- Affichage dynamique des données.

### Task 3 - Displaying Data from JSON or CSV Files in Flask

Lire des données stockées dans des fichiers JSON ou CSV et les afficher dans une page web.

Notions étudiées :

- Lecture de fichiers.
- Modules Python `json` et `csv`.
- Manipulation de listes et de dictionnaires.
- Transmission des données aux templates.

### Task 4 - Extending Dynamic Data Display to Include SQLite

Étendre l'application pour récupérer et afficher des données provenant d'une base SQLite.

Notions étudiées :

- Connexion à une base de données.
- Requêtes SQL.
- Récupération des résultats.
- Affichage des données dans des templates Flask.

## Principe du Server-Side Rendering

Le fonctionnement général du SSR peut être résumé en trois étapes :

1. Le navigateur envoie une requête au serveur.
2. Le serveur Python récupère les données et génère la page HTML à l'aide d'un template.
3. Le serveur renvoie le HTML au navigateur, qui affiche la page.

## Exemple de template Jinja

```html
<h1>Bonjour {{ name }}</h1>
```

Si Python transmet la valeur `name = "Bertrand"`, le navigateur reçoit le HTML généré :

```html
<h1>Bonjour Bertrand</h1>
```

L'expression `{{ name }}` est remplacée par la valeur de la variable transmise au template.

## Ressources officielles

- [Documentation Python](https://docs.python.org/3/)
- [Documentation Flask](https://flask.palletsprojects.com/)
- [Documentation Jinja](https://jinja.palletsprojects.com/)
- [Documentation Python - JSON](https://docs.python.org/3/library/json.html)
- [Documentation Python - CSV](https://docs.python.org/3/library/csv.html)
- [Documentation Python - SQLite](https://docs.python.org/3/library/sqlite3.html)
- [MDN - Server-side website programming](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side)

## Conclusion

Ce projet permet de comprendre comment Python peut être utilisé pour générer des pages web dynamiques, organiser les données et interagir avec différentes sources de stockage.

L'objectif est de maîtriser progressivement les bases du rendu côté serveur et de savoir les appliquer dans une application Flask.
