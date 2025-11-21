# Facciamo un semplice programma che controlli l'età del cliente e l'orario del giorno
# per verificare se possiamo o no vendergli alcolici

# Definiamo le regole:
#  * dopo le 21 non si vendono alcolici a nessuno
#  * Si vendono alcolici solo a chi ha almeno 18 anni
MAGGIORETA = 18  # Età dopo la quale diamo alcolici
ORARIO_CONSENTITO = 21  # Ora prima di cui diamo alcolici

eta_cliente = 19  # Età del cliente
orario = (0, 45)  # Tupla con orario (ore, minuti)

# 21 < 21 -> False
# 21 <= 21 -> True

if orario[0] < ORARIO_CONSENTITO:
    if eta_cliente >= MAGGIORETA:
        print("Serviamo alcolici al cliente")
    else:
        print("Non serviamo alcolici ai minorenni")
else:
    print("Dopo le 21 non serviamo alcolici")
print()

# Versione 2
# Lo stato ha deciso che l'orario massimo di servizio degli alcolici è 21:30
print("-" * 50)
# orario_rispettato = orario[0] < 21 or (orario[0] == 21 and orario[1] < 30)

ORARIO_DA_RISPETTARE = 21 * 60 + 30  # Ore convertite in minuti (* 60) + i minuti dell'orario
orario_convertito = orario[0] * 60 + orario[1]

orario_rispettato = orario_convertito < ORARIO_DA_RISPETTARE
if orario_rispettato:
    if eta_cliente >= MAGGIORETA:
        print("Serviamo alcolici al cliente")
    else:
        print("Non serviamo alcolici ai minorenni")
else:
    print("Dopo le 21:30 non serviamo alcolici")
print()
print("-" * 50)

# Variabili/costanti necessarie
ORARIO_MASSIMO_DA_RISPETTARE = 21 * 60 + 30  # Ore convertite in minuti (* 60) + i minuti dell'orario
ORARIO_MINIMO_DA_RISPETTARE = 8 * 60 + 30  # Ore convertite in minuti (* 60) + i minuti dell'orario

# Ci chiediamo se l'orario convertito è compreso tra i due consentiti
orario_rispettato = ORARIO_MINIMO_DA_RISPETTARE <= orario_convertito < ORARIO_MASSIMO_DA_RISPETTARE
# orario_rispettato = orario_convertito >= ORARIO_MINIMO_DA_RISPETTARE and orario_convertito < ORARIO_MASSIMO_DA_RISPETTARE
if orario_rispettato:
    if eta_cliente >= MAGGIORETA:
        print("Serviamo alcolici al cliente")
    else:
        print("Non serviamo alcolici ai minorenni")
else:
    print(f"Sono le {orario[0]}:{orario[1]}. Forniamo alcolici solo dalle 8:30 alle 21:30")
