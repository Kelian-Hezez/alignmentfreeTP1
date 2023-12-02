
# Alignment free - TP 1

L'objectif du TP est de comparer 5 especes de bactéries entre elles.
Vous trouverez les données en suivant [ce lien](https://we.tl/t-ACiDxJko7s)

## Composer le TP

Vous devez forker ce projet puis compléter ses fonctions.
Le rendu sera le dépot git dans lequel vous aurrez forké.

Le but est d'obtenir toutes les distances paire à paire des différentes bactéries.
Vous devez compléter le README pour y afficher la matrice des distances des bactéries.
Vous devez également y indiquer le temps d'exécution qu'il a fallu pour calculer cette matrice ainsi que l'espace mémoire maximale. Pour cela vous pouvez utiliser la commande ```/usr/bin/time -v```.

En observant les distances obtenues, que pouvez-vous dire des espèces présentes dans cet échantillon ?

## Résultats

Ce TME a été réalisé en binome par Ihsan Grichi et Kélian Hezez.

A=GCF_000006945.2_ASM694v2_genomic.fna
B=GCF_008244785.1_ASM824478v1_genomic.fna
C=GCF_014892695.1_ASM1489269v1_genomic.fna
D=GCF_020526745.1_ASM2052674v1_genomic.fna
E=GCF_020535205.1_ASM2053520v1_genomic.fna

Matrices des distances de Jaccard entre les différents génomes:

      A       B       C       D       E
A   1.000   0.938   0.002   0.019   0.018      
B   0.938   1.000   0.002   0.019   0.018
C   0.002   0.002   1.000   0.002   0.004
D   0.019   0.019   0.002   1.000   0.614
E   0.018   0.018   0.004   0.614   1.000

Nous avons fait deux version du script:
la première s'exécute en 68.51 secondes et utilise 430796 kO d'espace mémoire maximal.
La deuxième s'exécute en 60.39 secondes mais utilise 941308 kO d'espace mémoire maximal.

La deuxième version est donc plus rapide mais utilise plus d'espace mémoire, on peut donc choisir la version qui convient aux besoins de l'utilisateur.


Explication des résultats:

distance de jaccard: intersection des k-mers divisée par union des k-mers entre deux génomes. une distance égale à 1 reflète une identité complète entre les deux génomes. à l'inverse, une distance de 0 indique que les génomes ne partagent pas un seul k-mer.

le génome A et B proviennent de la même espèce (Salmonella enterica) mais de souches différentes, elles présentent quelques variation dans leur génome et notamment un plasmide supplémentaire dans le génome A. Cela explique la distance entre ces deux espèces de 0.938. Cela explique également les résultats très similaires quand on compare A et B aux autres génomes.
On retrouve le même cas de figure entre les génomes D et E qui sont des génomes d'Escherichia Coli de souches différentes. là aussi on a des distances qui felètent cette proximité.
En revanche quand on compare des génomes d'espèces différentes (comme C avec tous les autres génomes) on a des distances de jaccard très faibles.

Conclusion:
D'après ces comparaisons, la distance de jaccard est un indicateur cohérent de la distance génétique entre deux individus.