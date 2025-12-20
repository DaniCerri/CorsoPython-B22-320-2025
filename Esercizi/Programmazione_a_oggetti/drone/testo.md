# Ottimizza droni

La tua ditta di spedizioni a Neo-Tokyo è in crisi energetica e i superiori hanno ordinato di ridurre drasticamente il 
numero di decolli. Il tuo compito è scrivere il software per il "Dispatcher AI" centrale. Hai a disposizione tre 
classi: 
* `Package`: dati del pacco
* `DroneTrip`: rappresenta un singolo viaggio, ha una capacità massima di 100 kg e una lista di pacchi a bordo
* `FleetManager`: gestisce l'intera operazione

Il `FleetManager` riceve in input l'intera lista di pacchi dal JSON e deve allocarli creando il minor numero 
possibile di istanze di DroneTrip. 
Non basta caricare i pacchi in ordine di arrivo finché il drone è pieno: il sistema deve tentare di "incastrare" 
i pacchi in modo efficiente (ad esempio, se un drone ha 5kg liberi, deve cercare un pacco da 5kg o meno prima di 
chiudere il portellone e lanciarne uno nuovo). 
Al termine, il programma deve stampare un report che mostri quanti viaggi totali sono serviti, 
il peso trasportato da ogni singolo drone e la percentuale di spazio "sprecato" (spazio vuoto) per ogni viaggio.