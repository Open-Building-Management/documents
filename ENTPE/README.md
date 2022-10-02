 Dans les circuits à courant alternatif triphasé, on retrouve les trois types de puissances qu'on rencontre en monophasé :

 - la puissance active ou réelle (P) ;
 - la puissance réactive (Q) ;
 - la puissance apparente (S).

La puissance active est la puissance réellement disponible pour exécuter le travail. Elle se mesure en watts (W).

La puissance réactive représente la puissance engendrée par les éléments réactifs du circuit, qui sont des condensateurs (réactance capacitive) ou des bobines (réactance inductive). 
La puissance réactive ne consomme pas d'énergie, mais n'effectue aucun travail. Elle se mesure en voltampères réactifs (VARS).

La puissance apparente est la puissance totale fournie à la charge. Elle se mesure en voltampères (VA) et correspond à la somme vectorielle de la puissance active et de la puissance réactive du circuit.

L'équation suivante traduit cet énoncé de façon mathématique :

![image](https://user-images.githubusercontent.com/43913055/193457553-afc8a076-7829-4eed-82db-7bad5ffc7c8d.png)

# Calcul des puissances

Un récepteur triphasé n'est autre que trois récepteurs monophasés que l'on a branchés de façon particulière, étoile ou triangle, selon la source qui l'alimente.

La puissance d'un récepteur triphasé se détermine donc comme en monophasé pour chacun des récepteurs élémentaires.

Les récepteurs élémentaires fonctionnent indépendamment les uns des autres, leur puissance active et réactive vont donc s'additionner.

## Puissance active ou réelle 

Le principe de la conservation de l'énergie est appliqué : la puissance active totale est égale à la somme des puissance actives des trois récepteurs élémentaires 

P = P1 + P2 + P3.

Avec :

- P : puissance active du récepteur triphasé (en W).
- P1, P2 et P3 : puissances actives des récepteurs élémentaires (en W).

## Puissance réactive

La puissance réactive totale est égale à la somme des puissances réactives des trois récepteurs élémentaires.

Q = Q1 + Q2 + Q3

Avec: 
- Q : puissance réactive du récepteur triphasé (en VARS)
- Q1, Q2 et Q3 : puissances réactives des récepteurs élémentaires (en VARS)

## Puissance apparente

La puissance ne s'obtient jamais par addition des puissances apparentes, mais par l'utilisation de la formule :  

![image](https://user-images.githubusercontent.com/43913055/193457704-d88abc47-792f-45b3-b76b-233a2b7a68fe.png)

# Facteur de puissance

En monophasé, le facteur de puissance représente le déphasage entre le courant et la tension, déphasage causé par l'élément réactif du circuit. Il est défini par le cosinus du déphasage, comme le montre la figure suivante :

![image](https://user-images.githubusercontent.com/43913055/193457745-d7209009-5d3d-4dfa-bc44-467c26d181d8.png)


Pour déterminer le facteur de puissance à partir de la figure ci-dessus, nous devons connaître la valeur de la puissance apparente :

![image](https://user-images.githubusercontent.com/43913055/193457815-97168f29-259b-432a-919c-9c5c0c68b027.png)

Si :

![image](https://user-images.githubusercontent.com/43913055/193457858-446c14f8-afe8-4acd-b586-47c060c0013b.png)

On peut en déduire que :

![image](https://user-images.githubusercontent.com/43913055/193457872-2a05b0e6-0365-4b8d-975b-6a1362a5ee7b.png)

Le facteur de puissance n'est égal à un cosinus d'angle que si le récepteur est équilibré et si les courants et les tensions sont sinusoïdaux.
Si le récepteur est équilibré, en pourra donc écrire : 

![image](https://user-images.githubusercontent.com/43913055/193457917-a3e7fe17-dc0f-4949-a0af-43b4d2118d7c.png)

# Puissances dans un montage triphasé équilibré en étoile

Si le montage est équilibré, les récepteurs élémentaires sont:

- soumis à la même tension simple, donc de même valeur efficace V,
- traversés par des courants de même intensité efficace I,
- et ayant le même déphasage , donc le même facteur de puissance .

On a donc :

![image](https://user-images.githubusercontent.com/43913055/193458099-b0cf7153-2bf0-48eb-8da3-63b62a0dde81.png)

La puissance active du récepteur triphasé est donc : P = P1 + P2 + P3

Ou encore : 

![image](https://user-images.githubusercontent.com/43913055/193458073-3430eec4-1e19-439e-9cb8-3c636756a0a4.png)


Et si l'on remplace V par : 

![image](https://user-images.githubusercontent.com/43913055/193459352-cb45d95a-2f32-435d-a66d-d05fb3385cf8.png)

on obtient :

![image](https://user-images.githubusercontent.com/43913055/193459367-d43303d5-9537-4725-bb5f-587e583c33f0.png)
