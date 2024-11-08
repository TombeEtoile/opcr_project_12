# Epic Events CRM - Gestion d'Événements

## Description
Epic Events CRM est un logiciel de gestion de la relation client (CRM) développé pour Epic Events, une entreprise d'organisation d'événements. Ce CRM en ligne de commande facilite la gestion des clients, contrats et événements, ainsi que la communication entre les différents départements : Commercial, Support et Gestion.

## Fonctionnalités clés
- Gestion centralisée des clients, contrats, et événements
- Authentification des utilisateurs par identifiants uniques et permissions restreintes
- Filtrage personnalisé des données pour chaque équipe
- Suivi des événements par l'équipe support et des clients par l'équipe commerciale
- Principes de sécurité avancés pour minimiser les privilèges d'accès et éviter les injections SQL

## Contexte opérationnel
Les équipes d'Epic Events sont organisées en trois départements, chacun ayant des responsabilités spécifiques :

**Commercial :** Crée et gère les profils clients. Associe les événements aux clients.
**Support :** Supervise l'organisation des événements.
**Gestion :** Gère les collaborateurs, assure la création et la mise à jour des contrats.

## Exigences et spécifications techniques
**Langage :** Python 3.9 ou plus récent
**Interface :** Ligne de commande (CLI)

## Installation
### Prérequis
- Python 3.9+ installé
- Créez un environnement virtuel :
```
python -m venv venv
source venv/bin/activate  # Sous macOS et Linux
venv\Scripts\activate  # Sous Windows
```
### Installation des dépendances
- Clonez le dépôt GitHub :
```
git clone <URL_du_dépôt>
cd epic-events-crm
```
- Installez les dépendances :
```
pip install -r requirements.txt
```
### Initialisation de la base de données
```
python main.py init_db
```
### Utilisation
```
python main.py
```
### Authentification
Chaque collaborateur se connecte avec ses identifiants pour accéder aux fonctionnalités. En fonction de son rôle (commercial, support, ou gestion), différentes actions sont disponibles dans le menu principal.
Pour ajouter un collaborateur à la main, entrez la commande suivante :


## Fonctionnalités par rôle
1. Général
- Lecture seule de tous les clients, contrats, et événements.
- Connexion et déconnexion avec identifiants uniques pour chaque collaborateur.
2. Équipe de Gestion
- Collaborateurs : Création, mise à jour, suppression.
- Contrats : Création et mise à jour de tous les contrats.
- Événements : Filtrer et afficher les événements sans support associé, assigner des collaborateurs support, modifier les informations des événements.
3. Équipe Commerciale
- Clients : Création et mise à jour des clients associés.
- Contrats : Modification des contrats pour leurs clients.
- Événements : Créer un événement pour un client avec un contrat signé, filtrer les contrats non signés ou non payés.
4. Équipe Support
- Événements : Filtrage pour afficher uniquement les événements leur étant assignés, mise à jour des événements dont ils sont responsables.

## Permissions
Les permissions sont strictement définies pour chaque rôle afin de respecter le principe du moindre privilège :

- Équipe de Gestion : Accès total aux opérations sur les collaborateurs, contrats et événements.
- Équipe Commerciale : Accès restreint aux clients et contrats dont ils sont responsables.
- Équipe Support : Accès restreint à la mise à jour des événements leur étant assignés.

## Journalisation et suivi des erreurs
L’application utilise Sentry pour la journalisation des erreurs et des exceptions. Toutes les erreurs importantes sont consignées pour assurer une maintenance efficace et rapide.

## Sécurité
L’application suit les recommandations de sécurité :

- Prévention des injections SQL
- Gestion des sessions : Chaque utilisateur est authentifié, et un système de permissions limite l’accès aux fonctionnalités en fonction des besoins.
- Technologies
- Langage : Python
- Base de données : SQLite (pour stockage local)
- Journalisation des erreurs : Sentry

## Auteur
Développé par Augustin Verdier.
