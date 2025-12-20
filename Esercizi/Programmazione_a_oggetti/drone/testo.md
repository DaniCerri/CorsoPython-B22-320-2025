# Ottimizza droni

## Contesto
La tua ditta di spedizioni a Neo-Tokyo è in crisi energetica e i superiori hanno ordinato di ridurre drasticamente il numero di decolli. Il tuo compito è scrivere il software per il "Dispatcher AI" centrale.

## Classi da implementare

Hai a disposizione tre classi:

- **`Package`**: contiene i dati del pacco
- **`DroneTrip`**: rappresenta un singolo viaggio
  - Capacità massima: 100 kg
  - Contiene una lista di pacchi a bordo
- **`FleetManager`**: gestisce l'intera operazione di ottimizzazione

## Obiettivo

Il `FleetManager` riceve in input l'intera lista di pacchi dal JSON e deve allocarli creando il **minor numero possibile** di istanze di `DroneTrip`.

### Algoritmo di ottimizzazione

Non basta caricare i pacchi in ordine di arrivo finché il drone è pieno: il sistema deve tentare di "incastrare" i pacchi in modo efficiente.

**Esempio**: se un drone ha 5kg liberi, deve cercare un pacco da 5kg o meno prima di chiudere il portellone e lanciarne uno nuovo.

## Report finale

Al termine, il programma deve stampare un report che mostri:

1. Quanti viaggi totali sono serviti
2. Il peso trasportato da ogni singolo drone
3. La percentuale di spazio "sprecato" (spazio vuoto) per ogni viaggio