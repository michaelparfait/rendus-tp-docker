# TP Docker

### Exo3
Ecrire un fichier docker-compose.yml réunisssant 2 services
 - une application web basée sur une techno au choix (python/flask, nodejs/express, etc.)
 - un serveur mysql

Il existe de nombreux exemples sur le web permettant de comprendre rapidement comment intéragir avec une base de données depuis tel ou tel framework (exemple de recherche: "flash mysql")


L'application web exposera un endpoint unique '/ws/v1/user'

- requête en GET sur ce endpoint => on retourne au client un formulaire html permettant de saisir un nom d'utilisateur afin de l'enregistrer
- requête en POST sur ce endpoint => on récupère le nom de l'utilisateur posté et on l'enregistre en base
