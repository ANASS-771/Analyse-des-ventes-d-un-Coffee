# 📊 Sales Data Analysis & Visualization Tool

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-lightgrey?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-blue?logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)

## 📖 À propos du projet

Ce projet est une application en ligne de commande (CLI) développée en Python pour l'analyse exploratoire et la visualisation de données de ventes. 

Elle permet de charger un jeu de données brut, de le nettoyer, d'extraire des caractéristiques temporelles, de calculer des indicateurs clés (CA, quantités vendues) et de générer automatiquement une série de graphiques pertinents pour comprendre les tendances de vente.

## ✨ Fonctionnalités

L'application est structurée autour d'une classe principale `SalesApp` et propose un menu interactif avec les fonctionnalités suivantes :

*   **Importation & Aperçu :** Chargement des données depuis un fichier CSV, affichage des premières/dernières lignes, des types de données et des valeurs manquantes.
*   **Préparation des données :** 
    *   Conversion des colonnes de date et d'heure en un objet `datetime` unique.
    *   Extraction de nouvelles variables temporelles : heure, jour de la semaine, mois, année.
    *   Conversion automatique des types (numériques et catégoriels).
*   **Nettoyage :** Suppression des lignes avec des valeurs critiques manquantes et élimination des doublons.
*   **Analyse descriptive :** Calcul des statistiques de base (moyenne, écart-type, min, max) sur les quantités, prix unitaires et prix totaux.
*   **Analyse des ventes :** Calcul du chiffre d'affaires total et répartition par catégorie de produits.
*   **Visualisations graphiques :**
    *   Diagrammes à barres (CA par catégorie, par type de produit, quantités vendues).
    *   Graphiques combinés (Quantité et prix par catégorie).
    *   Analyse temporelle (Ventes par jour de la semaine, courbes des ventes et quantités par heure).
    *   Analyse par magasin (Barres et camemberts des ventes par emplacement).
*   **Exportation :** Sauvegarde des données nettoyées dans un nouveau fichier CSV.

## 🛠️ Technologies utilisées

*   **Langage :** Python 3
*   **Manipulation de données :** Pandas, NumPy
*   **Visualisation de données :** Matplotlib

## 📂 Format des données attendu

Le script s'attend à ce que le fichier CSV source (par défaut `datasett_.csv`) contienne au minimum les colonnes suivantes :
*   `transaction_date` (format : JJ/MM/AAAA)
*   `transaction_time` (format : HH:MM:SS)
*   `transaction_qty` (quantité vendue)
*   `unit_price` (prix unitaire)
*   `store_location` (emplacement du magasin)
*   `product_category` (catégorie du produit)
*   `product_type` (type de produit)
*   `product_detail` (détail du produit)

## 🚀 Installation et Lancement

### Prérequis
Assurez-vous d'avoir Python installé sur votre machine. Vous aurez également besoin des bibliothèques suivantes :

```bash
pip install pandas numpy matplotlib
