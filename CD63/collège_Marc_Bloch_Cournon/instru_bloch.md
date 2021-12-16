![Logo Cerema monochrome gris vertical](https://user-images.githubusercontent.com/24553739/146218239-e2dd560e-6edc-4f16-aa6e-d521975042d5.png)

# Instrumentation du collège Marc Bloch à Cournon

En février 2021, on a instrumenté 2 circuits desservant respectivement les ailes nord et sud de la sous-station ouest de l’externat (bâtiment d'enseignement).

Pour chaque circuit, on a mis en place :
- 2 PT100 pour apprécier les températures de départ et de retour de l'eau chaude
- un capteur au rez de chaussée et un autre à l'étage pour tenter d'objectiver le confort thermique

![bloch](https://user-images.githubusercontent.com/24553739/146335913-1ad28292-2b44-46b8-aa90-fdcd62b92b8a.png)


# Tour d'horizon des différentes stratégies de gestion de l'intermittence les plus courantes

Il existe principalement 4 grandes familles de programmation d'intermittence, toutes plus ou moins empiriques. Les réglages sont généralement effectués à dires d'expert.

## ralenti

Le ralenti consiste en un abaissement de courbe de chauffe pour les périodes d’inoccupation : en période d’inoccupation, on continue toujours à fournir en permanence de la chaleur au bâtiment, moins qu’en période d’occupation, mais en quantité suffisante pour ne pas permettre un abaissement rapide de la température intérieure.

Avec une production dimensionnée pour un régime d’eau 90/70°, on considère souvent qu’une variation de température d’eau de 4 à 5°C entraîne une variation de température ambiante de 1°C. 

Le décalage de courbe de chauffe est donc généralement de l'ordre de -20°C, afin de ne pas laisser la température intérieure descendre en dessous de 16°C (cas d'une consigne de 20°C pour la température intérieure)

## coupure et relance à heures fixes

- fonctionnement normal du chauffage en période d’occupation (par exemple loi d'eau sur la température extérieure)
- arrêt complet du chauffage (arrêt des chaudières, fermeture des vannes mélangeuses, arrêt des circulateurs, …) en fin de période d’occupation,
- relance du chauffage à allure réduite pendant la période d’inoccupation, par exemple si la température extérieure descend en dessous d'une certaine valeur limite. Les installations les plus récentes peuvent utiliser des sondes d'ambiance pour mesurer la température intérieure, et ainsi déclencher la relance si la température intérieure est en dessous de valeurs seuils (16° en semaine et 14° le week-end)
- relance du chauffage, à pleine puissance un peu avant l'ouverture des locaux.

## optimiseur non autoadaptatif

Par rapport à une stratégie avec horaires fixes, les optimiseurs ajustent quotidiennement le moment des coupures/relances en fonction de la température extérieure et de la température intérieure si elle est mesurée. 

Lorsqu’il fait plus chaud : 
- le refroidissement du bâtiment est plus lent : l'heure de coupure peut donc être avancée
- la température intérieure atteinte durant l’inoccupation est moins basse et l’énergie nécessaire à la relance est plus faible : l'heure de la relance peut donc être retardée.

La paramétrisation de ce type de programmateur reste délicate : en effet, il faut procéder par tatonnements, puisque plusieurs paramètres importants restent inconnus de l’utilisateur : l’inertie thermique du bâtiment, son isolation, le degré de surpuissance du chauffage. Seul un bon monitoring temps réel permet un ajustement adéquat. 

## optimiseur autoadaptatif

Le programmateur adapte automatiquement ses paramètres de réglage au jour le jour, en fonction des résultats qu’il a obtenu les jours précédents. 
**Par rapport à un optimiseur non autoadaptatif bien réglé, l’optimiseur autoadaptatif n’apportera pas d’économie d’énergie complémentaire. Son rôle est de faciliter (l’utilisateur ne doit plus intervenir) et donc d’optimaliser le réglage.**

L'auto-apprentissage semble séduisant à première vue, mais la pertinence des réglages dépendra de la qualité des échantillons de données qu'on fournira en entrée. Un bon monitoring est donc là-aussi indispensable pour s'assurer que l'algorithme n'apprend pas en se fondant sur des données peu représentatives.

## gestion de l'intermittence et économies d'énergie

D'une manière générale, si l'on veut faire des économies d'énergie, il est indispensable que le réseau hydraulique du bâtiment soit bien réglé. Procéder à un équilibrage des différentes zones de chaque circuit est une opération utile si l'on dispose de vannes d'équilibrage positionnées aux endroits stratégiques. En cas de déséquilibre prononcé sur un circuit, le pilotage doit se faire en utilisant comme témoin la zone où le confort thermique est le moins bon, au risque de dégrader le confort de manière prononcée. On parle de pilotage au plus défavorable, ce qui ne permet pas de maximiser les économies d'énergie.



