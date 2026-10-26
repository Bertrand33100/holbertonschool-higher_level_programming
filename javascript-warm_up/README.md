# JavaScript – Introduction

## Description

Ce projet fait partie de ma formation en développement informatique à **Holberton School**.

L'objectif de ce chapitre est de découvrir les fondamentaux du langage **JavaScript**, d'apprendre à écrire des scripts exécutables avec **Node.js** et de comprendre les concepts essentiels de la programmation.

JavaScript sera également utilisé par la suite pour rendre les pages web interactives, notamment dans le projet AirBnB.

## Objectifs d'apprentissage

À la fin de ce chapitre, je dois être capable de :

- Comprendre le rôle de JavaScript.
- Exécuter un script JavaScript avec Node.js.
- Déclarer des variables avec `var`, `let` et `const`.
- Identifier les différents types de données.
- Utiliser les opérateurs arithmétiques, logiques et de comparaison.
- Écrire des conditions avec `if`, `else if` et `else`.
- Utiliser les boucles `for` et `while`.
- Comprendre `break` et `continue`.
- Créer et utiliser des fonctions.
- Comprendre le rôle de `return`.
- Manipuler les tableaux et les objets.
- Comprendre la portée des variables (*scope*).
- Écrire des commentaires.
- Importer des fonctionnalités depuis un autre fichier.

## Technologies utilisées

| Technologie | Utilisation |
|---|---|
| JavaScript | Langage de programmation |
| Node.js | Exécution des scripts |
| npm | Gestionnaire de paquets |
| Semistandard | Vérification du style JavaScript |
| Ubuntu / WSL | Environnement de développement |
| Git / GitHub | Gestion et suivi du code |

### Versions de mon environnement

- Node.js : `22.22.1`
- npm : `11.12.1`
- Semistandard : `17.0.0`

**Remarque :** les consignes originales du projet Holberton prévoient Node.js 14.x et Semistandard 16.x.x. La compatibilité des versions installées avec les tests du projet reste à vérifier.

## Notions fondamentales

### 1. Variables et constantes

- `let` : déclare une variable pouvant être réaffectée.
- `const` : déclare une variable qui ne peut pas être réaffectée.
- `var` : ancienne syntaxe de déclaration de variables.

```javascript
let age = 30;
const language = 'JavaScript';

age = 31;
```

### 2. Types de données

Les principaux types étudiés sont :

- `String` : chaîne de caractères.
- `Number` : nombre.
- `Boolean` : vrai ou faux.
- `Undefined` : valeur non définie.
- `Null` : absence volontaire de valeur.
- `Object` : ensemble de propriétés.
- `Array` : collection ordonnée de valeurs.

JavaScript possède également les types primitifs `BigInt` et `Symbol`.

### 3. Conditions

Les conditions permettent d'exécuter différentes instructions selon une expression logique.

```javascript
const age = 18;

if (age >= 18) {
  console.log('Majeur');
} else {
  console.log('Mineur');
}
```

### 4. Boucles

Les boucles permettent de répéter des instructions.

```javascript
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```

- `for` : répétition contrôlée par une condition.
- `while` : répétition tant qu'une condition est vraie.
- `break` : arrêt d'une boucle.
- `continue` : passage à l'itération suivante.

### 5. Fonctions

Une fonction permet de regrouper des instructions réutilisables.

```javascript
function addition(a, b) {
  return a + b;
}

console.log(addition(5, 3));
```

Résultat : `8`

Une fonction sans instruction `return` renvoie `undefined`.

### 6. Tableaux

Les tableaux permettent de stocker plusieurs valeurs.

```javascript
const fruits = ['pomme', 'banane', 'orange'];

console.log(fruits[0]);
```

Résultat : `pomme`

Les index commencent à `0`.

### 7. Objets

Les objets permettent de stocker des informations sous forme de propriétés.

```javascript
const student = {
  name: 'Bertrand',
  school: 'Holberton'
};

console.log(student.name);
```

Résultat : `Bertrand`

### 8. Portée des variables

La portée (*scope*) détermine où une variable est accessible.

- `let` et `const` possèdent une portée de bloc.
- `var` possède une portée de fonction ou globale selon son contexte.

### 9. Modules

Dans l'environnement CommonJS de Node.js, il est possible d'exporter et d'importer des fonctionnalités avec :

- `module.exports`
- `require()`

Ces mécanismes permettent d'organiser un programme dans plusieurs fichiers.

## Exécution des scripts

Chaque fichier JavaScript du projet doit commencer par :

```javascript
#!/usr/bin/node
```

Pour rendre un fichier exécutable :

```bash
chmod +x fichier.js
```

Pour exécuter le script :

```bash
./fichier.js
```

Il est également possible de l'exécuter avec :

```bash
node fichier.js
```

## Vérification du style

Le projet utilise **Semistandard** pour contrôler la qualité et la cohérence du code.

Vérifier un fichier :

```bash
semistandard fichier.js
```

Vérifier les fichiers JavaScript du dossier courant :

```bash
semistandard
```

Les principales règles comprennent :

- Utiliser une indentation cohérente de deux espaces.
- Terminer les instructions par des points-virgules.
- Éviter les variables inutilisées.
- Respecter les règles de syntaxe et de style JavaScript.

## Exigences du projet Holberton

- Première ligne : `#!/usr/bin/node`.
- Fichiers exécutables.
- Chaque fichier doit se terminer par une nouvelle ligne.
- Présence obligatoire d'un `README.md` à la racine du projet.
- Respect des règles Semistandard.
- Compatibilité avec l'environnement d'évaluation demandé.

## Ressources

- [Documentation JavaScript – MDN](https://developer.mozilla.org/fr/docs/Web/JavaScript)
- [Guide JavaScript – MDN](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide)
- [Documentation Node.js](https://nodejs.org/docs/latest/api/)
- [JavaScript Semistandard](https://github.com/standard/semistandard)
- [JavaScript Standard Style](https://standardjs.com/)

## Conclusion

Ce chapitre constitue une première étape dans l'apprentissage de JavaScript.

Il permet de consolider les fondamentaux de la programmation : variables, conditions, boucles, fonctions, tableaux, objets et modules.

Ces connaissances serviront à développer des scripts plus complexes et à ajouter des fonctionnalités interactives aux applications web.

---

**Formation :** Holberton School  
**Chapitre :** JavaScript – Introduction  
**Langue :** Français