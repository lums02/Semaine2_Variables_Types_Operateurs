# Projet Fil Rouge - Santé Publique
## Semaine 2 : Variables, Types & Opérateurs

### 📌 Contexte
Cette semaine fait partie du programme Data Science d’Akieni Academy.  
Le projet simule une mission de conseil en data science pour le Ministère de la Santé du Congo.  
Objectif global : construire progressivement un pipeline complet (Python → SQL → Pandas → BI → ML).

### 🎯 Objectifs pédagogiques
- **Techniques** :
  - Déclarer et manipuler des variables Python avec des noms en `snake_case`
  - Utiliser les 4 types de base : `int`, `float`, `str`, `bool`
  - Réaliser des calculs arithmétiques avec les opérateurs (+, -, *, /, //, %, **)
  - Convertir les types avec `int()`, `float()`, `str()`, `type()`
  - Afficher des résultats formatés avec `f-strings`

- **Métier** :
  - Identifier les entités clés du système de santé congolais (patients, hôpitaux, consultations, médicaments)
  - Calculer des indicateurs sanitaires simples (taux, ratios, moyennes)
  - Comprendre l’impact du type de donnée sur les calculs

- **Analyse de données** :
  - Distinguer variables quantitatives (âge, coût, quantité) et qualitatives (sexe, diagnostic, ville)
  - Comprendre la granularité (patient vs hôpital)
  - Anticiper les erreurs de type (ex. âge stocké en `str`)

- **Communication** :
  - Produire un affichage structuré et lisible avec `print()` et `f-strings`
  - Commenter son code pour un collègue non-technicien
  - Nommer ses variables de façon expressive

### 📂 Structure du dépôt

Semaine2_Variables_Types_Operateurs/
│── README.md
│── exercice1_fiche_patient/
│   └── semaine2_exercice1_sante.py
│── ressources/ (optionnel : données PDF, consignes)



### 🧪 Exercices réalisés
1. **Exercice 1 : Fiche Patient du CHU de Brazzaville**
   - **Contexte** : Mme Celestine MAVOUNGOU, 42 ans, se présente aux urgences avec une forte fièvre. L’infirmier saisit ses informations dans le nouveau système.
   - **Code** : `exercice1_fiche_patient/semaine2_exercice1_sante.py`
   - **Résultat attendu** :
     - Calcul du coût total avec remise CNSS (10 500 FCFA)
     - Taux d’occupation des lits (88.8%)
     - Ratio consultations/médecin (2.6)
     - Affichage complet de la fiche patient avec f-strings

### 📊 Résultats & KPIs
- **Coût total** : 10 500 FCFA  
- **Taux d’occupation** : 88.8%  
- **Ratio consultations/médecin** : 2.6  
- **Statut** : Prise en charge validée

### 🚀 Instructions d’exécution
1. Cloner le dépôt :
   ```bash
   git clone https://github.com/ton-compte/Semaine2_Variables_Types_Operateurs.git
2. Se placer dans le dossier :
  ```bash
  cd Semaine2_Variables_Types_Operateurs
  ```
3. Exécuter le script :
  ```bash 
  python exercice1_fiche_patient/semaine2_exercice1_sante.py
  ```

### 👩🏽‍💻 Auteur

Projet réalisé par **Exaucée Lumeya Kwivangana** 
Programme Data Science – Akieni Academy, Brazzaville, 2026
