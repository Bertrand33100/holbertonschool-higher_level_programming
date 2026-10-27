# JavaScript DOM Manipulation

## Description

Ce projet de Holberton School permet de découvrir la manipulation du DOM (*Document Object Model*) avec JavaScript.

Le DOM représente la structure d'une page HTML sous forme d'objets accessibles depuis JavaScript. Il permet de sélectionner des éléments HTML, de modifier leur contenu et leur apparence, de créer ou supprimer des éléments et de réagir aux actions de l'utilisateur.

L'objectif est d'apprendre à rendre une page web interactive sans avoir à la recharger à chaque modification.

## Objectifs d'apprentissage

À la fin de ce projet, je dois être capable de :

- Sélectionner des éléments HTML avec `document.querySelector()` et `document.querySelectorAll()`.
- Comprendre la différence entre les sélecteurs par balise, identifiant (`id`) et classe (`class`).
- Modifier les styles CSS d'un élément depuis JavaScript.
- Lire et modifier le contenu d'un élément avec `textContent` et `innerHTML`.
- Créer, ajouter et supprimer des éléments dans le DOM.
- Écouter les événements utilisateur avec `addEventListener()`.
- Effectuer des requêtes HTTP avec `XMLHttpRequest` et l'API `fetch()`.
- Comprendre et corriger les erreurs JavaScript.

## Notions principales

### 1. Sélectionner un élément

La méthode `document.querySelector()` permet de sélectionner le premier élément correspondant à un sélecteur CSS.

Exemples de sélecteurs :

- `header` : sélection par nom de balise.
- `#titre` : sélection par identifiant.
- `.important` : sélection par classe.

### 2. Modifier un style CSS

La propriété `style` permet de modifier directement le style d'un élément HTML.

Exemple d'utilisation : changer la couleur du texte d'un élément.

### 3. Modifier le contenu

- `textContent` permet de lire ou remplacer le texte d'un élément.
- `innerHTML` permet de lire ou remplacer son contenu HTML.

Pour afficher du texte simple, `textContent` est généralement préférable.

### 4. Modifier la structure du DOM

Les méthodes `document.createElement()`, `appendChild()` et `remove()` permettent respectivement de créer, ajouter et supprimer des éléments HTML.

### 5. Gérer les événements

La méthode `addEventListener()` permet d'exécuter une fonction lorsqu'un événement se produit, par exemple lors d'un clic sur un bouton.

### 6. Effectuer des requêtes HTTP

`XMLHttpRequest` et `fetch()` permettent de communiquer avec un serveur pour récupérer ou envoyer des données.

## Exercices du projet

| Exercice | Objectif |
|---|---|
| 0. Color Me | Modifier la couleur du texte de la balise `header` en rouge (`#FF0000`). |

Les autres exercices seront ajoutés au fur et à mesure de leur réalisation.

## Contraintes techniques

- Utiliser JavaScript pour manipuler le DOM.
- Ne pas utiliser `var`.
- Respecter les règles de style Semistandard.
- Tester les fichiers dans Google Chrome.
- Terminer chaque fichier par une nouvelle ligne.
- Fournir un fichier `README.md` pertinent à la racine du projet.
- Éviter le rechargement de la page pour les interactions et les mises à jour du DOM.
- Demander une revue QA manuelle une fois le projet terminé.

## Environnement de travail

- JavaScript
- HTML5
- CSS
- Google Chrome
- WSL et terminal Linux
- Git et GitHub
- Semistandard
