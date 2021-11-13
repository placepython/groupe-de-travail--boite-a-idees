# Id3as: boite à idée de projets

Ce projet implémente une application de boîte à idée permettant de collecter des idées de projet via leur titre et une description courte optionnelle, de leurs affecter éventuellement des tags et des catégories, et de permettre à un utilisateur d'aimer (éventuellement DownVoter) ou de ne pas aimer (éventuellement UpVoter) pour manifester leur motivation ou non motivation pour le projet proposé.

Cette application utilise le framework django dans sa dernière version 3.2. L'idée est d'utiliser le moteur de template de django pour la réalisation du front-end avec Bootstrap pour apporter des styles simples.

## Installation

Les dépendances de ce projet sont gérée avec pipenv comme recommandé dans la documentation officielle de python. Pour ceux qui ne l'ont pas installé (si la commande `pipenv --version` vous donne une erreur), n'hésitez pas à l'installer à l'aide de pipx comme décrit dans [cette documentation](./docs/installer-pipenv.md). Une fois que pipenv est installé sur votre système, vous pouvez commencer le développement de ce projet en suivant les instruction ci-dessous:

1. Forkez le projet sur votre propre compte github
2. Cloner votre fork avec git pour obtenir une version locale
3. Ouvrez un terminal à la racine du projet
4. Installer les dépendances du projet avec `$ pipenv install --dev` (si pipenv n'est 
5. Activez l'environnement virtuel avec `$ pipenv shell`
6. Exécutez les migrations avec `$ python manage.py migrate`. La version de développement utiliser sqlite comme base de données. La version de production utilise postgresql.
7. Démarrez le serveur de développement avec `$ python manage.py runserver`

## Applications django

Le projet a déjà été découpé en applications django comme suit:

- **projects** implémente les idées de projets
- **pages** implémente les pages statiques du site
- **users** implémente le modèle utilisateur et le système d'authentification
- **profiles** implémente le profil utilisateur avec la posibilité de gérer les idées de projet qu'il a proposées
- **votes** implémente le système de vote sur les idées de projets
- **categories** implémente le système de catégories
- **tags** implémente le système de tags et utilise la biblithèque taggit pour son implémentation

Ces différentes applications ont été préconfigurées dans le squellette de départ.

