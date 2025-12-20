# Security Operation Center

## Contesto
Sei il responsabile di un SOC di cybersecurity che deve gestire un'ondata di attacchi hacker in tempo reale. Il tuo compito è smistare le minacce agli analisti corretti prima che i sistemi crollino.

## Classi da implementare

Hai bisogno di tre classi:

- **`Analyst`**: l'esperto umano
  - Nome
  - Specializzazione: Network, Crypto o Social
  - Livello di Skill: da 1 a 10
  - Livello di Stress: parte da 0

- **`Threat`**: la minaccia
  - Tipo (Network, Crypto, Social)
  - Gravità: da 1 a 10
  - ID univoco

- **`DefenseGrid`**: il sistema centrale di gestione

## Logica di assegnamento

Il tuo script deve caricare le minacce dal JSON e assegnarle seguendo queste regole:

1. Ogni minaccia deve essere assegnata a un analista con la **specializzazione corrispondente**

2. **Se Skill >= Gravità della minaccia**:
   - La minaccia viene neutralizzata (successo)
   - Lo stress dell'analista aumenta di **+1**

3. **Se Skill < Gravità**:
   - La minaccia "buca" il sistema (fallimento)
   - Lo stress dell'analista aumenta di **+5** per la frustrazione

4. **Burnout**: se lo stress di un analista supera **10**, va in burnout e non può più accettare ticket

## Report finale

L'obiettivo è processare l'intera lista e stampare un report finale con:

1. Minacce sventate vs minacce subite
2. Lo stato di salute mentale del team (stress di ogni analista)