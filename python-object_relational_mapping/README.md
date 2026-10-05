# Python - Object-Relational Mapping

## Description

Ce projet a pour objectif de découvrir comment **Python peut communiquer avec une base de données MySQL** et comment utiliser un **ORM (Object-Relational Mapper)** avec SQLAlchemy.

Le projet est divisé en deux grandes parties :

1. Utiliser **MySQLdb** pour communiquer directement avec MySQL et exécuter des requêtes SQL depuis Python.
2. Utiliser **SQLAlchemy**, un ORM, pour manipuler les données de la base de données avec des **objets Python**, sans écrire directement les requêtes SQL.

L'objectif est de comprendre le lien entre :

```text
Python
   │
   ├── MySQLdb ──────► SQL ──────► MySQL
   │
   └── SQLAlchemy ───► Objets Python ───► MySQL
```

---

# Objectifs d'apprentissage

À la fin de ce projet, je dois être capable d'expliquer :

- Comment connecter Python à une base de données MySQL.
- Comment récupérer des données MySQL depuis Python.
- Comment insérer des données dans MySQL depuis Python.
- Ce qu'est un ORM.
- Comment associer une classe Python à une table MySQL.
- Comment utiliser SQLAlchemy pour manipuler une base de données.
- Comment utiliser une session SQLAlchemy.
- Comment effectuer des opérations CRUD avec SQLAlchemy.

CRUD signifie :

| Opération | Signification | Exemple |
|---|---|---|
| **C** | Create | Ajouter une donnée |
| **R** | Read | Lire une donnée |
| **U** | Update | Modifier une donnée |
| **D** | Delete | Supprimer une donnée |

---

# 1. MySQLdb

## Qu'est-ce que MySQLdb ?

`MySQLdb` est un module Python permettant de se connecter à un serveur MySQL et d'exécuter des requêtes SQL.

Exemple de fonctionnement :

```text
Python
   │
   │ MySQLdb
   ▼
MySQL Server
   │
   ▼
Database
   │
   ▼
Table
```

Avec MySQLdb, je dois connaître SQL.

Par exemple :

```sql
SELECT * FROM states ORDER BY id ASC;
```

Python envoie cette requête à MySQL et récupère le résultat.

---

# 2. Connexion à MySQL

Une connexion nécessite généralement :

- l'adresse du serveur ;
- le port ;
- le nom d'utilisateur ;
- le mot de passe ;
- le nom de la base de données.

Dans ce projet, MySQL fonctionne sur :

```text
host = localhost
port = 3306
```

---

# 3. Cursor

Le **cursor** permet d'exécuter des requêtes SQL sur la connexion MySQL.

Le fonctionnement général est :

```text
Connexion
    │
    ▼
Cursor
    │
    ▼
Requête SQL
    │
    ▼
Résultat
```

Après utilisation, la connexion et le curseur doivent être fermés.

---

# 4. SELECT

Une requête `SELECT` permet de récupérer des données.

Exemple :

```sql
SELECT * FROM states;
```

Pour trier les résultats :

```sql
SELECT * FROM