# ============================================================ 
# AKIENI ACADEMY — Projet Sante Publique 
# Semaine 2 — Exercice 2 : KPIs Sanitaires OMS 
# ============================================================ 
 
# --- DONNEES BRUTES --- 
budget_fcfa          = 87_450_000   # underscore pour lisibilite des grands nombres 
nb_consultations_ext = 4823 
nb_hospitalisations  = 1247 
nb_deces             = 18 
nb_lits_total        = 180 
nb_lits_occupes      = 143 
nb_medecins          = 22 
nb_infirmiers        = 58 
population_dept      = 128_000 
taux_eur_fcfa        = 655.957 
taux_usd_fcfa        = 600.0 
 
# --- A COMPLETER --- 
# 1. Conversions devises 
budget_eur = 87450_000 / taux_eur_fcfa
budget_usd = 87450_000 / taux_usd_fcfa
 
# 2. Indicateurs OMS 
densite_medicale     = (nb_medecins/population_dept) * 1000
taux_mortalite       = (nb_deces / nb_hospitalisations) * 100
taux_occupation      = (nb_lits_occupes / nb_lits_total) * 100
 
# 3. Division entiere et modulo 
budget_medicaments   = int(budget_fcfa * 0.35) 
cout_journalier_meds = 450_000 
jours_stock          = budget_medicaments // cout_journalier_meds  # division entiere // 
jours_restants       = budget_medicaments % cout_journalier_meds   # modulo % 
 
# 4. Puissance pour projection 
budget_n_plus_2      = budget_fcfa * (1.8 ** 2) 
 
# --- AFFICHAGE RAPPORT --- 
print(f'=== RAPPORT TRIMESTRIEL Q4 2025 - Hopital General Pointe-Noire ===') 
print('BUDGET')
print(f'Depenses Q4 : {budget_fcfa:,} FCFA')
print(f'En euros : {budget_eur:,.2f} EUR')
print(f'En dollars : {budget_usd:,.2f} USD')

print('\nINDICATEURS OMS')
print(f'Densite medicale : {densite_medicale:.2f} medecins / 1000 hab [Norme OMS : >= 2.3]')
print(f'Taux mortalite : {taux_mortalite:.2f} % [Seuil alerte : > 2%]')
print(f'Taux occupation : {taux_occupation:.2f} % [Optimal : 70-80%]')

print('ANALYSE PHARMACIE')

print(f'Budget medicaments : {budget_medicaments:,} FCFA')
print(f'Jours de stock : {jours_stock} jours')
print(f'Jours depassement : {jours_restants} jours')

print("PROJECION")
print(f'Budget n+2 (8%/an) : {budget_n_plus_2:,.0f} FCFA')

print(f'ALERTE : Densite medicale CRITIQUE ({densite_medicale:.2f} pour 1000 hab — Norme OMS : >= 2.3)')