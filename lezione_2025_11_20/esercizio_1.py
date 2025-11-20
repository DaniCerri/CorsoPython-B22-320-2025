# Abbiamo una partita IVA, il nostro codice ATECO ci dice che l'imponibile è il 67% del fatturato
# Sull'imponibile paghiamo il 15% di IRPEF e il 26.07% di INPS
# Calcoliamo quanto paghiamo di IRPEF e di INPS in €
# Calcoliamo quale percentuale di fatturato ci rimane dopo le tasse

# Suggerimento:
# - il 27% di una variabile "numero" è: numero * 0.27
# - il 43.2% di una variabile "numero" è: numero * 0.432
# - lo 0.1% di una variabile "numero" è: numero * 0.001

# Suggerimento: le tasse nel contesto in cui siamo, non cambiano mai

fatturato = 123_123  # Fatturato in €
COEFF_IMPONIBILE = 0.67  # Il coefficiente dell'imponibile sul fatturato
COEFF_IRPEF = 0.15
COEFF_INPS = 0.2607


# Le tasse si pagano sull'imponibile
imponibile = fatturato * COEFF_IMPONIBILE  # Calcoliamo l'imponibile in base al fatturato

# Calcoliamo quanto paghiamo di IRPEF
quota_irpef = imponibile * COEFF_IRPEF

# Calcoliamo quanto paghiamo di INPS
quota_inps = imponibile * COEFF_INPS

# Primo modo di calcolare quanto rimane in percentuale dopo le tasse
netto = fatturato - (quota_irpef + quota_inps)  # Prima calcoliamo il netto dopo le tasse
coeff_netto = netto / fatturato # Calcoliamo il coeff di netto su fatturato, se lo vogliamo
# come percentuale "pura", facciamo ancora un * 100

# Secondo modo di calcora quanto rimane in percentuale dopo le tasse
coeff_irpef_sul_tot = COEFF_IRPEF * COEFF_IMPONIBILE
coeff_inps_sul_tot = COEFF_INPS * COEFF_IMPONIBILE

coeff_netto_2 = 1 - (coeff_inps_sul_tot + coeff_irpef_sul_tot)

# Stampiamo i risultati
print(f"Calcolo tasse e netto su un fatturato di {fatturato} €:")
print(f"Con un coeff di reddito di {COEFF_IMPONIBILE:.2%} e i coeff IRPEF e INPS a {COEFF_IRPEF:.2%} e {COEFF_INPS:.2%}")
print(f" - Contributo IRPEF: {quota_irpef:.2f} €")  # .2f -> arrotonda il risultato a 2 cifre decimali
print(f" - Contributo INPS: {quota_inps:.2f} €")
print(f" - Netto rimanente %: {coeff_netto:.2%} -> primo modo")  # .2% -> arrotonda la percentuale corrispondente al coeff a 2 cifre decimali e lo stampa come percentuale
print(f" - Netto rimanente %: {coeff_netto_2:.2%} -> secondo modo")
