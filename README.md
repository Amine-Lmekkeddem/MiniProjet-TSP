# Mini-projet TSP – Analyse expérimentale et formulations exactes

## 🎯 Objectifs généraux (Niveau Master)

Ce mini-projet s’inscrit dans le cadre d’une approche **méthodologique et expérimentale** du **problème du voyageur de commerce (Traveling Salesman Problem – TSP)**, problème NP-difficile fondamental en recherche opérationnelle et en optimisation combinatoire.

Les objectifs principaux sont :

- Comprendre et implémenter des **formulations mathématiques exactes** du TSP
- Exploiter des **instances de référence issues de TSPLib**
- Étudier l’impact de la **taille et de la structure des instances** sur les performances du solveur
- Comparer deux formulations exactes classiques (**MTZ et SSB**) en termes de :
  - complexité du modèle
  - temps de résolution
  - scalabilité pratique avec CPLEX

---

## 📌 Partie I – Étude expérimentale à partir de TSPLib

### Objectif scientifique

Cette partie vise à analyser empiriquement le comportement du solveur CPLEX sur des instances TSP de tailles croissantes, en se basant sur des données issues de **TSPLib**, référence internationale pour l’évaluation des algorithmes TSP.

### Méthodologie

- Génération et résolution d’instances de tailles variables (n = 5 à 45)
- Extraction systématique :
  - de la **distance totale optimale**
  - du **temps CPU**
- Analyse graphique :
  - distance totale en fonction de n
  - temps CPU en fonction de n (échelle logarithmique)

### Analyse

- La **distance totale optimale** n’évolue pas de manière monotone avec n, ce qui s’explique par la **distribution géométrique des points**.
- Le **temps CPU présente une forte variabilité**, avec des pics marqués pour certaines tailles (n = 25, 35), illustrant la **difficulté combinatoire intrinsèque** du TSP.
- Ces résultats confirment que la difficulté du TSP dépend autant de la **structure de l’instance** que de sa taille.

---

## 📌 Partie II – TP1 : Formulations exactes du TSP

### Exercice 4 – Formulation MTZ (Miller–Tucker–Zemlin)

#### Objectifs

- Implémenter la formulation MTZ en langage OPL
- Évaluer :
  - le nombre de variables de décision
  - le nombre de contraintes
- Résoudre les instances **bays29** et **eil51**

#### Analyse de complexité

- Variables :
  - \( n^2 \) variables binaires \( x_{ij} \)
  - \( n \) variables entières \( u_i \)
- Contraintes :
  - contraintes de degré : \( 2n \)
  - contraintes MTZ : \( (n-1)^2 \)

Complexité globale : **O(n²)**

#### Résultats

- Temps de résolution faibles
- Solutions optimales obtenues pour toutes les instances testées
- Très bonne stabilité numérique

---

### Exercice 5 – Formulation SSB (Sarin–Sherali–Bhootra)

#### Objectifs

- Implémenter la formulation SSB en OPL
- Comparer ses performances avec la formulation MTZ
- Étudier l’impact des contraintes de transitivité

#### Analyse de complexité

- Variables :
  - \( n^2 \) variables binaires \( x_{ij} \)
  - \( (n-1)^2 \) variables binaires \( u_{ij} \)
- Contraintes :
  - contraintes de transitivité en **O(n³)**

#### Résultats

- Les solutions obtenues sont optimales et identiques à celles de MTZ
- Le temps CPU augmente fortement dès que n dépasse 30
- Résolution très coûteuse pour **eil51**

---

## 📊 Comparaison MTZ vs SSB

| Critère | MTZ | SSB |
|-------|-----|-----|
| Optimalité | Oui | Oui |
| Temps CPU | Faible | Très élevé |
| Complexité théorique | O(n²) | O(n³) |
| Scalabilité | Bonne | Faible |
| Usage pratique | Recommandé | Limité |

---

## ✅ Conclusion générale (Niveau Master)

Ce travail met en évidence l’écart important qui peut exister entre **l’intérêt théorique d’une formulation** et son **efficacité computationnelle réelle**.

Bien que les formulations **MTZ et SSB soient équivalentes du point de vue de l’optimalité**, leurs performances pratiques diffèrent significativement :

- La formulation **MTZ** constitue un excellent compromis entre :
  - simplicité de modélisation
  - taille du modèle
  - efficacité de résolution avec un solveur MILP moderne
- La formulation **SSB**, malgré un encadrement théorique plus strict des sous-tours, souffre d’une **explosion combinatoire** due aux contraintes de transitivité, limitant fortement son applicabilité aux grandes instances.

Ces résultats illustrent un principe fondamental en optimisation combinatoire au niveau Master :
> *Une formulation plus forte théoriquement n’est pas nécessairement plus performante en pratique.*

---

## 📚 Références

- TSPLib – A Traveling Salesman Problem Library  
  https://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/
- Miller, C. E., Tucker, A. W., Zemlin, R. A. (1960). *Integer Programming Formulation of Traveling Salesman Problems*
- Sarin, S., Sherali, H. D., Bhootra, A. (2005). *New Tighter Polynomial Length Formulations for the Asymmetric TSP*

