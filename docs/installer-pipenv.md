# Installer pipenv de manière isolée à l'aide de pipx

Nous documentation vous emmêne pas à pas à travers l'installation de pipenv en utilisant le projet pipx permettant d'installer des outils 
python de manière isolée de votre système dans leur propre environnement virtuel. Ainsi, vous ne polluez votre installation de python et 
pouvez désinstaller de manière propre chaque outils installé. Ca fonctionne avec n'importe quel outils, que ce soit pipenv, flake8, black, 
pylint, mypy, docformatter, isort, etc. Il y en a des dizaines :)

## Première étape: installation de pipx lui-même

Voici les étapes pour installer pipx lui-même sur votre système. Vous n'avez pas besoin de le faire s'il est déjà présent sur votre os. Vous 
pouvez vérifier cela avec pipx --version dans un terminal. Si cette command retourne une erreur, pipx n'est pas installé. Sinon, c'est tout bon
et vous pouvez passer directement à la section suivante.

1. Installer pipx avec `$ pip install pipx`
2. Configurer la variable d'environnement PATH automatiquement avec `$ pipx ensurepath`
3. Déconnectez-vous de votre session utilisateur sur votre os et reconnectez-vous

Voilà, pipx est installé. Vous pouvez vérifier qu'il est fonctionnel en exécutant la commande `pipx --version` dans un terminal. Ca a fonctionné ? La commande `pipx install <nom de l'outils>` peut maintenant vous servir à installer n'importe quel
outils de développement présent sur PyPI.

## Seconde étape: installation de pipenv

Une fois que pipx est installé, l'installation de pipenv est immédiate et simple:

1. Excuter dans un terminal la commande `$ pipx install pipenv`
2. Vérifier l'installation avec `$ pipenv --version`

Voilà, pipenv est installé sur votre système et vous pouvez continuer avec la [lecture du README.md](../README.md).
