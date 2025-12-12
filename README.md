# Challenge Triple A - Dashboard de Monitoring
## Description :

Le Challenge Triple A consiste à créer un outil simple de monitoring pour une machine Linux. À l’aide de scripts Python, le projet collecte différentes informations système et les affiche dans un tableau de bord web en HTML/CSS. L’objectif est de combiner administration Linux, algorithmique Python et affichage web dans une solution légère et compréhensible.

## Prérequis :

Une machine sous Ubuntu Desktop 22.04 LTS ou plus récent, Python 3, un accès Internet et la bibliothèque Python psutil sont nécessaires pour faire fonctionner le projet.

## Installation :

Après avoir cloné le dépôt GitHub, il suffit d’installer les dépendances Python requises. Aucune configuration supplémentaire n’est nécessaire.

# Commandes pour installer les dépendances :

sudo apt update
sudo apt install python3-pip -y
pip install psutil

## Utilisation :
# Comment lancer le script

Le script principal se lance depuis le terminal :

Depuis VS Code


Si aucun dossier n’est précisé, le dossier personnel de l’utilisateur est analysé par défaut.

# Ouvrir index.html dans le navigateur

Une fois le script exécuté, le fichier index.html généré peut être ouvert directement dans un navigateur pour afficher le dashboard.

## Fonctionnalités

Le projet affiche les informations système générales, l’utilisation du CPU et de la mémoire, les processus les plus gourmands en ressources ainsi qu’une analyse des fichiers d’un dossier donné selon leurs extensions.

## Captures d'écran

Des captures du terminal et du dashboard final sont disponibles dans le dossier screenshots.

## Difficultés rencontrées

Les principales difficultés concernent l’utilisation de la bibliothèque psutil, la gestion des fichiers Python séparés et la prise en main de Git et GitHub.

## Améliorations possibles

Le projet peut être amélioré avec un rafraîchissement automatique, des codes couleur, des jauges graphiques ou une interface web dynamique.

## Auteur

Projet réalisé par AGGAB Mohammed, BERDEJO Alexandre et AVERBOUCH Guillaume dans le cadre du Challenge Triple A.
