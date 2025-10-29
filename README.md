# Analyse de sentiments sur Twitter avec Apache Spark et Scala

## Objectif du projet
Ce projet a été réalisé dans le cadre de la formation à **CY Tech** afin d’explorer l’utilisation d’**Apache Spark** pour le traitement distribué de données textuelles.  
L’objectif principal était de classifier des tweets selon leur tonalité (positive, neutre ou négative) et de visualiser les relations entre les mots à l’aide d’un graphe de co-occurrences.

---

## Contexte et présentation
L’analyse des sentiments est un domaine clé du **traitement automatique du langage naturel (NLP)**.  
Nous avons utilisé **Spark MLlib** pour l’apprentissage automatique et **GraphX** pour la modélisation de graphes à grande échelle.  

Ce projet illustre la puissance de Spark pour :
- traiter efficacement de grandes quantités de données textuelles ;
- construire un pipeline complet de machine learning (prétraitement → vectorisation → classification) ;
- explorer la sémantique des textes via des graphes.

---

## Méthodologie

### 1. Collecte des données
Les données proviennent de **Kaggle**, et concernent des tweets liés à la compagnie aérienne *Virgin America*.  
Nous avons conservé un échantillon de **100 tweets** pour réduire le temps de calcul.

### 2. Prétraitement
- Nettoyage du texte (tokenisation, suppression des stopwords)
- Vectorisation via **CountVectorizer**
- Indexation des labels (StringIndexer)

### 3. Modélisation
- Modèle : **Régression logistique (Logistic Regression)**  
- Outil : **Spark MLlib**
- Implémentation en **Scala**

### 4. Visualisation
Les co-occurrences de mots ont été représentées sous forme de graphe avec **GraphX** et **Plotly**.

---

## Résultats

- Classification réussie des tweets en trois classes : *positif*, *neutre* et *négatif*  
- Visualisation de clusters de mots reflétant les associations les plus fréquentes  
- Construction d’un graphe de connexions sémantiques, révélant les relations contextuelles entre les termes.

*(Voir le rapport PDF pour les graphiques et interprétations détaillés.)*

---

## Fichiers inclus
| Fichier | Description |
|----------|-------------|
| `Code_Scala.txt` | Script principal en Scala utilisant Spark pour l’analyse des sentiments |
| `Graphe_plotly.py` | Script Python pour la visualisation interactive des graphes |
| `Tweets.csv` | Jeu de données réduit de tweets annotés |
| `Rapport_Scala_Groupe_4.pdf` | Rapport complet du projet, méthodologie et résultats |

---

## Auteurs
Projet réalisé par :  
**Iyad Ben Mosbah**, **Othmane Aboussaad**, **Kenza Mouharrar**, **Samuel Zerrouk**  
(Encadré dans le cadre du module *Big Data & Spark* – CY Tech)

---

## Mots-clés
`Apache Spark` · `Scala` · `GraphX` · `MLlib` · `Analyse de Sentiments` · `NLP` · `Big Data`

---

## Références
- [Documentation Spark](https://spark.apache.org/)  
- [Documentation Scala](https://docs.scala-lang.org/)
