# ============================================================ 
# AKIENI ACADEMY — Projet Sante Publique 
# Semaine 2 — Exercice 1 : Fiche Patient CHU Brazzaville 
# Votre nom : LUMEYA KWIVANGANA Exaucée 
# Date      : 26/06/2026
# ============================================================ 
 
# --- SECTION 1 : VARIABLES HOPITAL District Kinkala --- 

hopital1 = "Hopital District Kinkala"
budget_hopital1 = 12_500_000
consultations_hopital1 = 1_847
hospitalisations_hopital1 = 312
deces_hospitaliers_hopital1 = 8
lits_total_hopital1 = 45
lits_occupes_hopital1 = 41
medecins_permanents_hopital1 = 3
population_desservie_hopital1 = 85_000

# --- SECTION 2 : VARIABLES HOPITAL CMS de Vindza --- 

hopital2 = "CMS de Vindza"
budget_hopital2 = 6_800_000
consultations_hopital2 = 923
hospitalisations_hopital2 = 87
deces_hospitaliers_hopital2 = 2
lits_total_hopital2 = 20
lits_occupes_hopital2 = 14
medecins_permanents_hopital2 = 1
population_desservie_hopital2 = 42_000

# --- SECTION 3 : VARIABLES HOPITAL de Kindamba  --- 

hopital3 = "Hopital de Kindamba"
budget_hopital3 = 9_200_000 
consultations_hopital3 = 1_243
hospitalisations_hopital3 = 201
deces_hospitaliers_hopital3 = 11
lits_total_hopital3 = 35
lits_occupes_hopital3 = 33
medecins_permanents_hopital3 = 2
population_desservie_hopital3 = 67_000

# --- SECTION 4 : CALCULS ET INDICATEURS ---
# TODO : Calculer pour chaque hopital : cout moyen par patient, taux d'occupation, densite medicale, taux de mortalite

# Calculs pour Hopital District Kinkala
cout_moyen_par_patient_hopital1  = budget_hopital1 / consultations_hopital1
taux_occupation_hopital1 = (lits_occupes_hopital1 / lits_total_hopital1) * 100
densite_medicale_hopital1 = (medecins_permanents_hopital1 / population_desservie_hopital1) * 1000
taux_mortalite_hopital1 = (deces_hospitaliers_hopital1 / hospitalisations_hopital1) * 100

# Calculs pour CMS de Vindza
cout_moyen_par_patient_hopital2  = budget_hopital2 / consultations_hopital2
taux_occupation_hopital2 = (lits_occupes_hopital2 / lits_total_hopital2) * 100
densite_medicale_hopital2 = (medecins_permanents_hopital2 / population_desservie_hopital2) * 1000
taux_mortalite_hopital2 = (deces_hospitaliers_hopital2 / hospitalisations_hopital2) * 100

# Calculs pour Hopital de Kindamba
cout_moyen_par_patient_hopital3  = budget_hopital3 / consultations_hopital3
taux_occupation_hopital3 = (lits_occupes_hopital3 / lits_total_hopital3) * 100
densite_medicale_hopital3 = (medecins_permanents_hopital3 / population_desservie_hopital3) * 1000
taux_mortalite_hopital3 = (deces_hospitaliers_hopital3 / hospitalisations_hopital3) * 100

# --- SECTION 5 : RAPPORT (Produire un rapport consolide formate avec f-strings, comparable et lisible par un non-technicien )---

print(40*'=')

print(f'{"Objet : Rapport comparatif urgent — 3 hopitaux du departement du Pool":^40}')

print(40*'=')

print(f'Hopital : {hopital1}')
print(f'Budget : {budget_hopital1:,}')
print(f'Consultations : {consultations_hopital1}')
print(f'Hospitalisations : {hospitalisations_hopital1}')
print(f'Décès hospitaliers : {deces_hospitaliers_hopital1}')
print(f'Lits totaux : {lits_total_hopital1}')
print(f'Lits occupés : {lits_occupes_hopital1}')
print(f'Médecins permanents : {medecins_permanents_hopital1}')
print(f'Population desservie : {population_desservie_hopital1:,}')
print(f'Coût moyen par patient : {cout_moyen_par_patient_hopital1:.2f}')
print(f'Taux d\'occupation : {taux_occupation_hopital1:.2f}%')
print(f'Densité médicale : {densite_medicale_hopital1:.2f}')
print(f'Taux de mortalité : {taux_mortalite_hopital1:.2f}%')
if taux_mortalite_hopital1 > 2 or densite_medicale_hopital1 < 0.05:
    print("ALERTE : Hopital 1 en situation critique !")


print(40*'_')
print(f'Hopital : {hopital2}')
print(f'Budget : {budget_hopital2:,}')
print(f'Consultations : {consultations_hopital2}')
print(f'Hospitalisations : {hospitalisations_hopital2}')
print(f'Décès hospitaliers : {deces_hospitaliers_hopital2}')
print(f'Lits totaux : {lits_total_hopital2}')
print(f'Lits occupés : {lits_occupes_hopital2}')
print(f'Médecins permanents : {medecins_permanents_hopital2}')
print(f'Population desservie : {population_desservie_hopital2:,}')
print(f'Coût moyen par patient : {cout_moyen_par_patient_hopital2:.2f}')
print(f'Taux d\'occupation : {taux_occupation_hopital2:.2f}%')
print(f'Densité médicale : {densite_medicale_hopital2:.2f}')
print(f'Taux de mortalité : {taux_mortalite_hopital2:.2f}%')
if taux_mortalite_hopital2 > 2 or densite_medicale_hopital2 < 0.05:
    print("ALERTE : Hopital 2 en situation critique !")
print(40*'_')

print(f'Hopital : {hopital3}')
print(f'Budget : {budget_hopital3:,}')
print(f'Consultations : {consultations_hopital3}')
print(f'Hospitalisations : {hospitalisations_hopital3}')
print(f'Décès hospitaliers : {deces_hospitaliers_hopital3}')
print(f'Lits totaux : {lits_total_hopital3}')
print(f'Lits occupés : {lits_occupes_hopital3}')
print(f'Médecins permanents : {medecins_permanents_hopital3}')
print(f'Population desservie : {population_desservie_hopital3:,}')
print(f'Coût moyen par patient : {cout_moyen_par_patient_hopital3:.2f}')
print(f'Taux d\'occupation : {taux_occupation_hopital3:.2f}%')
print(f'Densité médicale : {densite_medicale_hopital3:.2f}')
print(f'Taux de mortalité : {taux_mortalite_hopital3:.2f}%')
if taux_mortalite_hopital3 > 2 or densite_medicale_hopital3 < 0.05:
    print("ALERTE : Hopital 3 en situation critique !")
print(40*'_')



# BONUS :  calculer si le budget total des 3 hopitaux suffit pour passer a 5 medecins chacun (cout d'un medecin : 1 200 000 FCFA/trimestre) 

budget_total = budget_hopital1 + budget_hopital2 + budget_hopital3
cout_total_nouveaux_medecins = 5 * 1_200_000    # 5 medecins, 1_200_000 FCFA/trimestre (coût pour 3 mois)
if budget_total >= cout_total_nouveaux_medecins:
    print("BONUS : Le budget total des 3 hopitaux suffit pour embaucher 5 nouveaux médecins !")
else:
    print("BONUS : Le budget total des 3 hopitaux ne suffit pas pour embaucher 5 nouveaux médecins.")