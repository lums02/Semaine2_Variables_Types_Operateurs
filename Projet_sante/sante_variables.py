# ============================================================ 
# MODULE FONDATEUR — Projet Sante Publique / Akieni Academy 
# Ce fichier centralise toutes les constantes et variables metier 
# Il sera enrichi chaque semaine jusqu'a S24 
# nom de l'auteur : LUMEYA KWIVANGANA Exaucée
# Date de creation : 26/06/2026
# ============================================================ 

# === SECTION A : CONSTANTES NATIONALES ET NORMES OMS ======== 
TAUX_EUR_FCFA = 655.957 
TAUX_USD_FCFA = 600.0 
SEUIL_OMS_DENSITE_MEDICALE = 2.3    
# medecins pour 1000 habitants 
SEUIL_OMS_COUVERTURE_VACCIN = 95.0  # pourcentage minimum OMS
SEUIL_MORTALITE_ALERTE = 2.0        # % deces / hospitalisations 
SEUIL_RUPTURE_STOCK_JOURS = 30      # jours minimum de stock 
DEPARTEMENTS_CONGO = [              # 12 departements officiels 
    'Brazzaville', 'Pointe-Noire', 'Bouenza', 'Cuvette', 
    'Cuvette-Ouest', 'Kouilou', 'Lekoumou', 'Likouala', 
    'Niari', 'Plateaux', 'Pool', 'Sangha' 
] 
 
# === SECTION B : VARIABLES DES 5 HOPITAUX =================== 
# Hopital 1 — CHU de Brazzaville 
h1_nom              = 'CHU de Brazzaville' 
h1_ville            = 'Brazzaville' 
h1_departement      = 'Brazzaville' 
h1_type             = 'CHU' 
h1_nb_lits          = 320 
h1_nb_lits_occupes  = 284 
h1_nb_medecins      = 47 
h1_nb_infirmiers    = 123 
h1_population_zone  = 1_800_000

# Hopital 2 — General de Pointe-Noire
h2_nom              = 'Hopital General Pointe-Noire' 
h2_ville            = 'Pointe-Noire' 
h2_departement      = 'Pointe-Noire' 
h2_type             = 'Hopital General' 
h2_nb_lits          = 150 
h2_nb_lits_occupes  = 130 
h2_nb_medecins      = 25 
h2_nb_infirmiers    = 60 
h2_population_zone  = 800_000 

# Hopital 3 — de Dolosie
h3_nom              = 'Hopital de Dolosie' 
h3_ville            = 'Dolosie' 
h3_departement      = 'Pool' 
h3_type             = 'Hopital Regional' 
h3_nb_lits          = 100 
h3_nb_lits_occupes  = 85 
h3_nb_medecins      = 15 
h3_nb_infirmiers    = 40 
h3_population_zone  = 500_000 

# Hopital 4 —  de district Owando
h4_nom              = 'Hopital de district Owando' 
h4_ville            = 'Owando'
h4_departement      = 'Sangha' 
h4_type             = 'Hopital de district' 
h4_nb_lits          = 80 
h4_nb_lits_occupes  = 65 
h4_nb_medecins      = 12 
h4_nb_infirmiers    = 30 
h4_population_zone  = 400_000 

# Hopital 5 —   Centre de sante de Impfondo
h5_nom              = 'Centre de sante de Impfondo'
h5_ville            = 'Impfondo'
h5_departement      = 'Sangha'
h5_type             = 'Centre de sante'
h5_nb_lits          = 60
h5_nb_lits_occupes  = 50
h5_nb_medecins      = 10
h5_nb_infirmiers    = 25
h5_population_zone  = 300_000

# === SECTION C : VARIABLES DES 5 MEDICAMENTS ================ 
# TODO : Declarer les 5 medicaments essentiels 

# Medicament 1 — Artemether-Lumefantrine
med1_nom = 'Artemether-Lumefantrine'
med1_quantite_disponible = 1000
med1_seuil_rupture = 100
med1_cout = 5000

# Medicament 2 — Amoxicilline
med2_nom = 'Amoxicilline'
med2_quantite_disponible = 1500
med2_seuil_rupture = 200
med2_cout = 3000

# Medicament 3 — Paracetamol
med3_nom = 'Paracetamol'
med3_quantite_disponible = 2000
med3_seuil_rupture = 250
med3_cout = 2000

# Medicament 4 — SRO
med4_nom = 'SRO'
med4_quantite_disponible = 1000
med4_seuil_rupture = 100
med4_cout = 4000

# Medicament 5 — Vaccin antipaludéen
med5_nom = 'Vaccin antipaludéen'
med5_quantite_disponible = 500
med5_seuil_rupture = 50
med5_cout = 6000

# === SECTION D : CALCULS D'INITIALISATION =================== 
# TODO : Calculer les KPIs globaux initiaux 
# CALCULS D'INITIALISATION : calculer et afficher au demarrage les KPIs globaux initiaux (densite medicale nationale, taux d'occupation moyen, valeur totale du stock de medicaments) 

# Calcule  KPIs globaux initiaux Hopital 1
h1_densite_medicale = (h1_nb_medecins / h1_population_zone)*1000
h1_taux_occupation = h1_nb_lits_occupes / h1_nb_lits

# Calcule  KPIs globaux initiaux Hopital 2
h2_densite_medicale = (h2_nb_medecins / h2_population_zone)*1000
h2_taux_occupation = h2_nb_lits_occupes / h2_nb_lits

# Calcule  KPIs globaux initiaux Hopital 3
h3_densite_medicale = (h3_nb_medecins / h3_population_zone)*1000
h3_taux_occupation = h3_nb_lits_occupes / h3_nb_lits

# Calcule  KPIs globaux initiaux Hopital 4
h4_densite_medicale = (h4_nb_medecins / h4_population_zone)*1000
h4_taux_occupation = h4_nb_lits_occupes / h4_nb_lits

# Calcule  KPIs globaux initiaux Hopital 5
h5_densite_medicale = (h5_nb_medecins / h5_population_zone)*1000
h5_taux_occupation = h5_nb_lits_occupes / h5_nb_lits


valeur_stock = med1_cout * med1_quantite_disponible + med2_cout * med2_quantite_disponible + med3_cout * med3_quantite_disponible + med4_cout * med4_quantite_disponible + med5_cout * med5_quantite_disponible

# === SECTION E : RAPPORT D'INVENTAIRE ======================= 
# TODO : Afficher le rapport initial du systeme de sante

print(60*'=')
print("RAPPORT D'INVENTAIRE INITIAL")
print(60*'=')

print(f"Valeur totale du stock de médicaments : {valeur_stock} FCFA")
print(60*'-')

print(f'HOPITAL : {h1_nom}')
print(f'Ville : {h1_ville}')
print(f'Departement : {h1_departement}')
print(f'Type : {h1_type}')
print(f'Nombre de lits : {h1_nb_lits}')
print(f'Nombre de lits occupés : {h1_nb_lits_occupes}')
print(f'Nombre de médecins : {h1_nb_medecins}')
print(f'Population desservie : {h1_population_zone}')
print(f'Densité médicale : {h1_densite_medicale:.2f} médecins pour 1000 habitants')
print(f'Taux d\'occupation : {h1_taux_occupation:.2%}')
print(60*'-')

print(f'HOPITAL : {h2_nom}')
print(f'Ville : {h2_ville}')
print(f'Departement : {h2_departement}')
print(f'Type : {h2_type}')
print(f'Nombre de lits : {h2_nb_lits}')
print(f'Nombre de lits occupés : {h2_nb_lits_occupes}')
print(f'Nombre de médecins : {h2_nb_medecins}')
print(f'Population desservie : {h2_population_zone}')
print(f'Densité médicale : {h2_densite_medicale:.2f} médecins pour 1000 habitants')
print(f'Taux d\'occupation : {h2_taux_occupation:.2%}')
print(60*'-')

print(f'HOPITAL : {h3_nom}')
print(f'Ville : {h3_ville}')
print(f'Departement : {h3_departement}')
print(f'Type : {h3_type}')
print(f'Nombre de lits : {h3_nb_lits}')
print(f'Nombre de lits occupés : {h3_nb_lits_occupes}')
print(f'Nombre de médecins : {h3_nb_medecins}')
print(f'Population desservie : {h3_population_zone}')
print(f'Densité médicale : {h3_densite_medicale:.2f} médecins pour 1000 habitants')
print(f'Taux d\'occupation : {h3_taux_occupation:.2%}')
print(60*'-')

print(f'HOPITAL : {h4_nom}')
print(f'Ville : {h4_ville}')
print(f'Departement : {h4_departement}')
print(f'Type : {h4_type}')
print(f'Nombre de lits : {h4_nb_lits}')
print(f'Nombre de lits occupés : {h4_nb_lits_occupes}')
print(f'Nombre de médecins : {h4_nb_medecins}')
print(f'Population desservie : {h4_population_zone}')
print(f'Densité médicale : {h4_densite_medicale:.2f} médecins pour 1000 habitants')
print(f'Taux d\'occupation : {h4_taux_occupation:.2%}')
print(60*'-')

print(f'HOPITAL : {h5_nom}')
print(f'Ville : {h5_ville}')
print(f'Departement : {h5_departement}')
print(f'Type : {h5_type}')
print(f'Nombre de lits : {h5_nb_lits}')
print(f'Nombre de lits occupés : {h5_nb_lits_occupes}')
print(f'Nombre de médecins : {h5_nb_medecins}')
print(f'Population desservie : {h5_population_zone}')
print(f'Densité médicale : {h5_densite_medicale:.2f} médecins pour 1000 habitants')
print(f'Taux d\'occupation : {h5_taux_occupation:.2%}')
print(60*'-')

print(f'MEDICAMENT : {med1_nom}')
print(f'Quantité disponible : {med1_quantite_disponible}')
print(f'Prix unitaire : {med1_cout} FCFA')
print(60*'-')

print(f'MEDICAMENT : {med2_nom}')
print(f'Quantité disponible : {med2_quantite_disponible}')
print(f'Prix unitaire : {med2_cout} FCFA')
print(60*'-')

print(f'MEDICAMENT : {med3_nom}')
print(f'Quantité disponible : {med3_quantite_disponible}')
print(f'Prix unitaire : {med3_cout} FCFA')
print(60*'-')

print(f'MEDICAMENT : {med4_nom}')
print(f'Quantité disponible : {med4_quantite_disponible}')
print(f'Prix unitaire : {med4_cout} FCFA')
print(60*'-')

print(f'MEDICAMENT : {med5_nom}')
print(f'Quantité disponible : {med5_quantite_disponible}')
print(f'Prix unitaire : {med5_cout} FCFA')
print(60*'=')   