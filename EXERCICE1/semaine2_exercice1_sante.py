# ============================================================ 
# AKIENI ACADEMY — Projet Sante Publique 
# Semaine 2 — Exercice 1 : Fiche Patient CHU Brazzaville 
# Votre nom : LUMEYA KWIVANGANA Exaucée 
# Date      : 25/06/2026
# ============================================================ 
 
# --- SECTION 1 : VARIABLES PATIENT --- 
# TODO : Declarer toutes les variables patient ci-dessous 
nom_patient = 'MAVOUNGOU Celestine'
try : 
    age_patient = int(input("Entrez l'âge du patient : "))
except ValueError:
    print("Veuillez entrer un âge valide.")
    exit()
sexe_patient = 'F'
departement_patient = 'Brazzaville'
couverture_sociale = 'CNSS'
 
# --- SECTION 2 : VARIABLES CONSULTATION --- 
# TODO : Declarer les variables consultation 
type_consultation = 'Urgences'
try :
    cout_consultation_fcfa = float(input("Entrez le coût de la consultation (en FCFA) : ")) 
    nb_consultations = int(input("Entrez le nombre de consultations : "))
except ValueError:
    print("Veuillez entrer des valeurs valides.")
    exit()
remise_cnss_pct = 30.0 
diagnostic_principal = 'Paludisme grave'
 
# --- SECTION 3 : VARIABLES HOPITAL --- 
# TODO : Declarer les variables hopital 
nom_hopital = 'CHU de Brazzaville'
ville_hopital = 'Brazzaville'
nb_lits_total = 320 
nb_lits_occupes = 284 
nb_medecins_actifs = 47
 
# --- SECTION 4 : CALCULS --- 
# TODO : Calculer le cout total apres remise CNSS 
cout_total_fcfa = cout_consultation_fcfa * nb_consultations * (1 - remise_cnss_pct / 100) 
 
# TODO : Calculer le taux d'occupation (en pourcentage, arrondi a 1 decimale) 
taux_occupation_pct = (round(nb_lits_occupes / nb_lits_total * 100, 1))
 
# TODO : Calculer le ratio consultations par medecin (ce jour) 
# Hypothese : 120 consultations ont eu lieu ce matin dans tout l'hopital 
nb_consultations_hopital = 120 
ratio_consultations_medecin = round(nb_consultations_hopital / nb_medecins_actifs, 1) 
 
# --- SECTION 5 : AFFICHAGE --- 
# TODO : Afficher une fiche complete avec f-strings 
print('='*60) 
print(f'  FICHE PATIENT — {nom_patient}') 
print('='*60) 
# ... completez l'affichage

print(f'Age : {age_patient} ans')
print(f'Sexe  : {sexe_patient}')
print(f'Departement : {departement_patient}')
print(f'Couverture : {couverture_sociale}')

print('_'*60)

print( "CONSULATION")
print(f'Type : {type_consultation}')
print(f'Diagnostic : {diagnostic_principal}')
print(f'Coût unitaire : {cout_consultation_fcfa} FCFA')
print(f'Remise CNSS : {remise_cnss_pct}%')
print(f'Coût total : {cout_total_fcfa} FCFA')


print('_'*60)

print(f'Hopital : {nom_hopital}')
print(f'Ville : {ville_hopital}')
print(f'Lits occupés : {nb_lits_occupes} / {nb_lits_total} ({taux_occupation_pct}%)')
print(f'Médecins actifs : {nb_medecins_actifs}')
print(f'Ratio consultations par médecin : {ratio_consultations_medecin}')

print('='*60) 

print(" STATUT : Prise en charge validée ")

print('='*60)