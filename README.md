# 🧠 Mini-projet TSP – Analyse expérimentale et formulations exactes

## 📌 Description

Ce mini-projet porte sur l’étude du **Traveling Salesman Problem (TSP)**, un problème classique NP-difficile en optimisation combinatoire.  
L’objectif est d’analyser expérimentalement le comportement du solveur CPLEX et de comparer deux formulations exactes du TSP.

---

## 🎯 Objectifs

- Implémenter des formulations mathématiques exactes du TSP
- Exploiter des instances de référence (TSPLib)
- Analyser l’impact de la taille des instances sur les performances
- Comparer les formulations **MTZ** et **SSB**

---

## 🚀 Partie I – Étude expérimentale

### 🔍 Méthodologie
- Génération d’instances (n = 5 à 45)
- Mesure :
  - Distance optimale
  - Temps CPU
- Analyse graphique (évolution en fonction de n)

### 📊 Résultats
- La distance dépend de la distribution des villes
- Le temps CPU augmente fortement avec la taille
- Présence de pics liés à la complexité combinatoire

---

## 🧮 Partie II – Formulations exactes

### 🔹 MTZ (Miller–Tucker–Zemlin)
- Complexité : O(n²)
- Résolution rapide
- Bonne scalabilité
- Modèle efficace

### 🔹 SSB (Sarin–Sherali–Bhootra)
- Complexité : O(n³)
- Résolution lente
- Scalabilité faible
- Coût computationnel élevé

---

## 📊 Comparaison

| Critère        | MTZ        | SSB         |
|---------------|-----------|-------------|
| Optimalité    | ✅        | ✅          |
| Temps CPU     | Faible    | Élevé       |
| Complexité    | O(n²)     | O(n³)       |
| Scalabilité   | Bonne     | Faible      |

---

## ⚙️ Technologies utilisées

- Langage : OPL
- Solveur : IBM ILOG CPLEX
- Données : TSPLib


---

## ✅ Conclusion

Les deux formulations permettent d’obtenir des solutions optimales, mais leurs performances diffèrent fortement.

- **MTZ** offre un bon compromis entre simplicité et efficacité
- **SSB** est plus coûteuse et moins adaptée aux grandes instances

👉 Une formulation plus forte théoriquement n’est pas toujours la plus performante en pratique.

