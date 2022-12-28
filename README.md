# Projet MI 2022 : Mélange de cartes

## Sommaire
1. [Introduction et informations](README.md#introduction-et-informations)
2. [Fonctionnalités](README.md#fonctionnalités)
3. [Compilation, exécution et arguments possibles](README.md#compilation-execution-et-arguments-possibles)
4. [Rapides explications des lois](README.md#rapides-explications-des-lois)

-------------------------------------------------------



## Introduction et informations
**Informations généraux**
- Le sujet du projet : [projet.pdf](/Documents/projet.pdf)

**Identifiants et membres du groupe**
1. NEDJAI Etienne, 21952852
2. TANG Elody, 21953199



## Fonctionnalités


**Mélange de cartes : k-insertion :**

Le travail réalisé sur le mélange de cartes avec la méthode de mélange "k-insertion" se trouve dans le dossier `/k-insertion/`.

**Fonctionnalités :**
1. Calcul des temps des remontées de la dernière carte et affichage de son histogramme
2. Téléchargement des histogrammes (des temps) dans le répertoire `/k-insertion/simulations/`
3. Affichage et interprétation de l'espérance du temps entre deux remontées de la dernière carte
4. Affichage et interprétation de la mesure invariante de la loi P_n (*)
5. Affichage et interprétation de la mesure invariante de la loi Q_n (**)


**Mélange de cartes : riffle-shuffle  |  Mélange à l'américaine :**

Le travail réalisé sur le mélange de cartes avec la méthode de mélange "riffle-shuffle" (qu'on appelle aussi le mélange à l'américaine) se trouve dans le dossier `/riffle-shuffle/`.

**Fonctionnalités :**`
1. Affichage et interprétation de la mesure invariante de la loi P_n pour des petites valeurs de taille de cartes (*)
2. Affichage et interprétation de la mesure invariante de la loi Q_n (**)
3. Affichage et interprétation de la mesure invariante de la loi P_n pour des grandes valeurs de taille de cartes, calculée avec une formule mathématique (*)



## Compilation execution et arguments possibles


**Mélange de cartes : k-insertion :**

**1.** Aller dans le dossier `cd /k-insertion/`.

**2.** Exécuter le fichier Python : `python3 exercice1.py [-OPTION1] [ARG1] [-OPTION2]...`

**3.** Mise en place et explication des arguments :

`[-OPTION1]` peut avoir un argument et peut être de la forme :
- "-taille" : pour spécifier la taille du paquet de cartes
- "-temps" : pour spécifier le temps entre deux remontées

`[-OPTION2]` ne peut pas avoir d'argument et peut être de la forme :
- "-esperance" : pour afficher l'espérance de T
- "-mesureX" : pour afficher la mesure invariante de la loi X_n (*)
- "-mesureY" : pour afficher la mesure invariante de la loi Y_n (**)
- "-h" pour afficher un message d'aide


**Mélange de cartes : riffle-shuffle  |  Mélange de cartes :**

**1.** Aller dans le dossier `cd /riffle-shuffle/`.

**2.** Exécuter le fichier Python : `python3 riffle.py [-OPTION1] [ARG1] [-OPTION2]...`

**3.** Mise en place et explication des arguments :

`[-OPTION1]` peut avoir un argument et peut être de la forme :
- "-taille" : pour spécifier la taille du paquet de cartes

`[-OPTION2]` ne peut pas avoir d'argument et peut être de la forme :
- "-mesureX" : pour afficher la mesure invariante de la loi X_n (*)
- "-mesureY" : pour afficher la mesure invariante de la loi Y_n (**)
- "-mesureXFormula" : pour afficher la mesure invariante de la loi X_n (*)
- "-h" pour afficher un message d'aide



## Rapides explications des lois


On dispose d’un jeu de r cartes initialement dans une pile. On a numéroté les cartes de 1 à r : la carte numéro 1 est celle initialement en haut du tas.


**Mélange de cartes : k-insertion :**

On arrange les cartes en prenant celle du dessus et en l’insérant uniformément en k entre la k-ème et la k + 1-ème, ce qu’on appelle la k-insertion.

**1. Étude de la loi P_n (\*)**

On note (P_n, n ≥ 0) la suite de permutations obtenues.


**2. Étude de la loi Q_n (\*\*)**

On suit les positions successives de l’une des cartes de notre paquet au
cours de notre mélange. On note (Q_n, n ≥ 0) la suite de ces positions (de sorte que si Q_0 = i, on suit la carte qui se trouve initialement en i-ème position). La loi invariante de cette loi est la loi uniforme.


**Mélange de cartes : riffle-shuffle  |  Mélange de cartes :**

On coupe le jeu au niveau de la M-ème carte. On ”re-mélange” nos 2 paquets (on préserve, bien sûr l’ordre relatif dans chacun des 2 sous-paquets). On appelle ça le mélange à l'américaine (ou le riffle-shuffle).

**1. Étude de la loi P_n (\*)**

On note (Q_n, n ≥ 0) la suite de permutations de {1, ... , r} obtenue.

**2. Étude de la loi Q_n (\*\*)**

À chaque carte du jeu, on attribue une étiquette entre 0 et 1. Puis on replace alors les cartes étiquetées 0 en haut du paquet. On note (Q_n , n ≥ 0) la suite de permutations de {1, ..., r} obtenue.

