# Développement Front-end

## Installation des dépendances

Les dépendances front-end peuvent être installées automatiquement à l'aide du
Node Package Manager (npm). Si node.js n'est pas installé sur votre ordinateur, 
installez-le depuis le site officiel. 

Une fois que node.js est installé et la commande `npm --version` s'exécute sans
erreur, vous pouvez installer les dépendances à l'aide des commandes suivantes lancées dans le
terminal depuis la racine du projet:

- `$ pipenv run python manage.py webpack`

Cette commande va créer un répertoire node_modules avec l'ensemble des
dépendances du front-end. Elle va aussi exécuter webpack pour générer les fichiers
statique à partir du code javascript et css défini dans assets/src/.

## Outils pour le développement du front-end

Le projet utilise webpack pour le développement front-end de l'application.
Si vous travailler sur le développement du front, deux répertoires sont
importants pour vous:

- **templates** contient l'ensemble des templates de l'application classés par app
- **assets** contient le code javascript et scss dans assets/src/index.js et assets/src/scss/styles.scss, respectement.

Vous pouvez ajouter vos fichiers statiques (typescript, javascript, scss, images, polices) directement
dans le répertoire assets/src/ et les importer ensuite dans assets/src/index.js.
Pour compiler votre code, on peut utiliser une des commandes suivantes:

- Pour compiler les fichiers statiques manuellement `$ pipenv run python manage.py webpack`
- Pour que les fichiers statiques se compilent automatiquement lorsque vous modifiez un fichier `$ pipenv run python manage.py webpack --watch`
