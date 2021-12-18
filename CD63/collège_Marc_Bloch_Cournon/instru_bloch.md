![Logo Cerema monochrome gris vertical](https://user-images.githubusercontent.com/24553739/146218239-e2dd560e-6edc-4f16-aa6e-d521975042d5.png)

# Instrumentation du collège Marc Bloch à Cournon et analyse de la performance énergétique d'hiver

En février 2021, on a instrumenté 2 circuits desservant respectivement les ailes nord et sud de la sous-station ouest de l’externat (bâtiment d'enseignement).

Pour chaque circuit, on a mis en place :
- 2 PT100 pour apprécier les températures de départ et de retour de l'eau chaude
- un capteur au rez de chaussée et un autre à l'étage pour tenter d'objectiver le confort thermique

![bloch](https://user-images.githubusercontent.com/24553739/146335913-1ad28292-2b44-46b8-aa90-fdcd62b92b8a.png)


# Tour d'horizon des différentes stratégies de gestion de l'intermittence les plus courantes

Il existe principalement 4 grandes familles de programmation d'intermittence, toutes plus ou moins empiriques. Les réglages sont généralement effectués à dires d'expert.

## Ralenti

Le ralenti consiste en un abaissement de courbe de chauffe pour les périodes d’inoccupation : en période d’inoccupation, on continue toujours à fournir en permanence de la chaleur au bâtiment, moins qu’en période d’occupation, mais en quantité suffisante pour ne pas permettre un abaissement rapide de la température intérieure.

Avec une production dimensionnée pour un régime d’eau 90/70°, on considère souvent qu’une variation de température d’eau de 4 à 5°C entraîne une variation de température ambiante de 1°C. 

Le décalage de courbe de chauffe est donc généralement de l'ordre de -20°C, afin de ne pas laisser la température intérieure descendre en dessous de 16°C (cas d'une consigne de 20°C pour la température intérieure)

## Coupure et relance à heures fixes

- fonctionnement normal du chauffage en période d’occupation (par exemple loi d'eau sur la température extérieure)
- arrêt complet du chauffage (arrêt des chaudières, fermeture des vannes mélangeuses, arrêt des circulateurs, …) en fin de période d’occupation,
- relance du chauffage à allure réduite pendant la période d’inoccupation, par exemple si la température extérieure descend en dessous d'une certaine valeur limite. Les installations les plus récentes peuvent utiliser des sondes d'ambiance pour mesurer la température intérieure, et ainsi déclencher la relance si la température intérieure est en dessous de valeurs seuils (16° en semaine et 14° le week-end)
- relance du chauffage, à pleine puissance un peu avant l'ouverture des locaux.

## Optimiseur non autoadaptatif

Par rapport à une stratégie avec horaires fixes, les optimiseurs ajustent quotidiennement le moment des coupures/relances en fonction de la température extérieure et de la température intérieure si elle est mesurée. 

Lorsqu’il fait plus chaud : 
- le refroidissement du bâtiment est plus lent : l'heure de coupure peut donc être avancée
- la température intérieure atteinte durant l’inoccupation est moins basse et l’énergie nécessaire à la relance est plus faible : l'heure de la relance peut donc être retardée.

La paramétrisation de ce type de programmateur reste délicate : en effet, il faut procéder par tatonnements, puisque plusieurs paramètres importants restent inconnus de l’utilisateur : l’inertie thermique du bâtiment, son isolation, le degré de surpuissance du chauffage. Seul un bon monitoring temps réel permet un ajustement adéquat. 

## Optimiseur autoadaptatif

Le programmateur se règle automatiquement au jour le jour, en fonction des résultats qu’il a obtenu les jours précédents. 
**Par rapport à un optimiseur non autoadaptatif bien réglé, l’optimiseur autoadaptatif n’apportera pas d’économie d’énergie complémentaire. 
Son rôle est de trouver tout seul les bons réglages, sans nécessiter d'intervention humaine.**

L'auto-apprentissage semble séduisant à première vue, mais la pertinence des réglages dépendra de la qualité des échantillons de données qu'on fournira en entrée. Un bon monitoring est donc là-aussi indispensable pour s'assurer que l'algorithme n'apprend pas en se fondant sur des données peu représentatives.

## Gestion de l'intermittence et économies d'énergie

D'une manière générale, si l'on veut faire des économies d'énergie, il est indispensable que le réseau hydraulique du bâtiment soit bien réglé. 

Procéder à un équilibrage des différentes zones de chaque circuit est une opération utile si l'on dispose de vannes d'équilibrage positionnées aux endroits stratégiques. 
En cas de déséquilibre prononcé sur un circuit, le pilotage sur la base de données de temperature intérieure doit se faire en utilisant comme témoin la zone où le confort thermique est le moins bon, au risque de dégrader le confort de manière prononcée. 

On parle de **pilotage au plus défavorable**, ce qui ne permet pas de maximiser les économies d'énergie.

# De la stratégie d'intermittence suivie par les régulateurs de la sous-station ouest de l’externat

La stratégie déployée à Marc Bloch ne repose pas sur des mesures de température intérieure pour réguler la distribution de l'eau chaude. On est donc plutôt sur un système de type coupure et relance à heures fixes. 

Le graphique ci-dessous représente la température d'eau chaude distribuée lors de la première semaine de chauffage sur la saison 2021/2022.

![](https://user-images.githubusercontent.com/24553739/146343944-e885fa67-7bbd-41e7-a009-a19d54203e22.png)

Le chauffage est actif le vendredi, coupé dans la soirée puis le dimanche, le fonctionnement réduit commence. On constate une coupure du réduit dans l'après-midi du dimanche, certainement en raison d'une météo clémente puis une reprise vers 21 h en soirée. 

Ce sont ensuite des cycles journaliers de 12h qui se succèdent, commencant à 6h du matin pour se terminer à 6 heures du soir. 

## journée du 11 octobre 2021

![](https://user-images.githubusercontent.com/24553739/146344774-1b142efb-3b0a-4793-85af-b69d1d8fcc5c.png)

## journée du 14 décembre 2021

![](https://user-images.githubusercontent.com/24553739/146346683-401bde83-13e3-4d87-aa10-25da4165b407.png)

Le système fonctionne à pleine puissance jusqu'à 8h puis de manière réduite ensuite, certainement suivant une loi d'eau de distribution. **En semaine, le chauffage est coupé la nuit. Il n'y a pas de ralenti et le système compte sur la relance à pleine puissance du matin pour avoir la bonne température à l'ouverture du bâtiment.**

# Analyse du confort thermique

Le chauffage a été mis en route le 8 octobre et l'hiver s'est installé véritablement début novembre 2021 : pour les 6 semaines depuis début novembre, les températures extérieures sont inférieures à 10°C près de 90% du temps

![](https://user-images.githubusercontent.com/24553739/146554347-043b7257-4f8d-484f-978c-7c53a8e4a2b6.png)

## Circuit nord

![](https://user-images.githubusercontent.com/24553739/146536002-9da5e0e2-b554-4d60-9d94-16ddf1c81941.png)

La différence de température entre le départ et le retour n'est pas perceptible. Ce disfonctionnement est imputable à une vanne de pression différentielle défaillante entre le départ et le retour. Celà a été vérifié lors d'une visite sur site le 17 décembre 2021 : la vanne semble bloquée en position ouverte. On peut envisager :
- de remplacer la vanne
- de l'effacer et de mettre en place des bouchons
A noter que la vanne de pression différentielle sur le circuit ne semble pas en meilleur état, mais la vanne n'est pas bloquée en position ouverte.

![](https://user-images.githubusercontent.com/24553739/146538391-21cd6cac-ea91-4a62-a25d-ac8d57914bd1.png)

On constate beaucoup de chutes de températures dues aux directives d'aération COVID, notamment dans la salle de technologie de l'étage (B209). Ces phénomènes viennent perturber la lecture des graphiques.

Lors des coupures nocturnes, la température au rez-de-chaussée descend jusqu'à 15°C alors qu'à l'étage le minimum est voisin de 18°C, sauf s'il y a eu une aération très efficace dans la journée. Cet écart entre étage et rez-de-chaussée est très certainement du à une meilleure isolation des combles, la chaleur ayant une tendance naturelle à monter.

L'effet des réduits de week-end est très perceptible : dès que le réduit se met en oeuvre, la température intérieure se stabilise à 19°C au rez-de-chaussée et à 20°C à l'étage. Le système n'a alors guère d'effort à faire pour être à la bonne température le lundi matin. Ce réduit pourrait être abaissé ou retardé car la puissance disponible pour remonter en température semble suffisante.

D'une manière générale, le confort est assez contrasté : on constate que lors de l'occupation du bâtiment, les températures ne sont pas à plus de 60% dans la zone confort, entre 19 et 21°C.

Salle de technologie<br>B209 | ![](https://user-images.githubusercontent.com/24553739/146554010-65cbdec6-7035-461f-b6c1-384178cfae7d.png)
--|--
<b>Salle de musique<br>B101<b> | ![](https://user-images.githubusercontent.com/24553739/146555284-d42b982d-1099-4532-b213-2058df919086.png)
  
### Cas de la mi-saison

Avant la mise en route du chauffage, on peut percevoir un certain inconfort dans le bâtiment au niveau de l'aile nord : 16°C au rez-de-chaussée et 17°C à l'étage à 8 heures du matin

![](https://user-images.githubusercontent.com/24553739/146561280-12ad152b-542b-4cc7-9a45-37aa86b36a4f.png)

## Circuit Sud

![](https://user-images.githubusercontent.com/24553739/146581831-2637e1a8-0742-4beb-bded-6f66e663c80b.png)

Le circuit fonctionne correctement et lors de la distribution de chaleur, on perçoit nettement un delta de température entre départ et retour de l'ordre de 10°C.

![](https://user-images.githubusercontent.com/24553739/146582169-b99507ea-3fb9-4ca7-8d64-94df714824d2.png)

Lors des coupures nocturnes, l'écart entre l'étage et le rez-de-chaussée est moins important que sur l'aile nord : 1°C seulement alors qu'on peut avoir 4 à 5°C côté nord.

En général, la température intérieure ne descend pas en dessous de 17°C, mis à part les périodes d'aération COVID.
  
Comme au nord, le réduit d'innocupation semble très confortable.
