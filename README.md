# Pays en chiffres
## Introduction
Manipulations des données sur les pays avec Python et Mongodb  

## Pré-requis  
Base de données Mongodb  
Python (veuillez installer les librairies requises dans le fichier requirements.txt pour lancer cet API)

## Procedure à suivre afin de lancer les scripts
1. **Lancer l'application**  
Executer le fichier src/main.py poutr lancer l'api

2. **Requetes HTTP**  
2.1. Récuperer la liste des pays  
`http://localhost:5000/countries/all`  
2.2. Retourner le pays qui correspond au critère passé en paramètre. Ce paramètre est le nom du pays  
`http://localhost:5000/countries/one/<pays>`  
2.3. Inserer un nouveau pays avec des données random (on précise uniquement le pays), et mise à jour de la date de modification  
`http://localhost:5000/countries/new/<pays>`  
2.4. Récuperer la liste des pays avec la tranche  
`http://localhost:5000/countries/by_tranche`  

les pays ont été regroupé sous les tranches de densité de population designées dans le tableau suivant:  
Densité de population | Tranche  
--- | ---  
< 100 | Tranche 1  
100 à 1000 | Tranche 2  
1001 à 10000| Tranche 3  
10001 < | Tranche 4  
