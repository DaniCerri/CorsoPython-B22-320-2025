# Security Operation Center

Sei il responsabile di un SOC di cybersecurity che deve gestire un'ondata di attacchi hacker in tempo reale. 
Il tuo compito è smistare le minacce agli analisti corretti prima che i sistemi crollino. 
Hai bisogno di tre classi: 
* Analyst: l'esperto umano, che ha un nome, una specializzazione tra Network, Crypto o Social, un livello di "Skill" da 
1 a 10 e un livello di "Stress" che parte da 0
* Threat: la minaccia, definita da un tipo, una gravità da 1 a 10 e un ID
* DefenseGrid: il sistema centrale 

Il tuo script deve caricare le minacce dal JSON e assegnarle. La logica è la seguente: ogni minaccia deve essere 
assegnata a un analista con la specializzazione corrispondente. 
Se l'analista ha una Skill >= Gravità della minaccia, la neutralizza (successo) ma il suo stress aumenta di 1. 
Se la Skill < Gravità, la minaccia "buca" il sistema (fallimento) e lo stress dell'analista aumenta di 5 per la 
frustrazione. Se lo stress di un analista supera 10, va in burnout e non può più accettare ticket. 
L'obiettivo è processare l'intera lista e stampare un report finale con: minacce sventate vs subite e lo stato 
di salute mentale del team.