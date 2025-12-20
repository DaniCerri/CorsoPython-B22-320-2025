"""
Il team di Risk Management sospetta che ci siano gruppi di utenti fittizi ("Sybil ring")
gestiti dalla stessa persona fisica; ci hanno fornito i log di accesso (utenti_metadata)
e le transazioni finanziarie (transazioni) chiedendoti di sviluppare un algoritmo
che raggruppi gli utenti in "Super-Identità" univoche basandosi sulla transitività delle
connessioni (ovvero: se A condivide un IP/Device con B, e B condivide un IP/Device con C,
allora A, B e C appartengono tutti alla stessa Super-Identità anche se A e C non hanno
nulla in comune direttamente) e, una volta mappati questi cluster, generare un report che
evidenzi esclusivamente le transazioni "Cross-Cluster", ovvero quei movimenti di denaro
che avvengono tra due Super-Identità completamente distinte, le quali sono le uniche che ci
interessano per le indagini di riciclaggio.
"""


def trova_super_identita(utenti_metadata):
    """
    Raggruppa gli utenti in Super-Identità basandosi sulla transitività delle connessioni.

    Args:
        utenti_metadata: Dizionario con dati IP e device_id per ogni utente

    Returns:
        Dizionario che mappa ogni utente alla sua Super-Identità (ID cluster)
    """
    # Creiamo una mappa: IP/Device -> lista di utenti che lo usano
    ip_to_users = {}
    device_to_users = {}

    for utente, dati in utenti_metadata.items():
        # Processa gli IP
        for ip in dati["ip"]:
            if ip not in ip_to_users:
                ip_to_users[ip] = []
            ip_to_users[ip].append(utente)

        # Processa i device
        for device in dati["device_id"]:
            if device not in device_to_users:
                device_to_users[device] = []
            device_to_users[device].append(utente)

    # Inizializza ogni utente nel proprio cluster
    utente_a_cluster = {utente: utente for utente in utenti_metadata.keys()}

    def trova_root(utente):
        """Trova il rappresentante del cluster (con path compression)"""
        if utente_a_cluster[utente] != utente:
            utente_a_cluster[utente] = trova_root(utente_a_cluster[utente])
        return utente_a_cluster[utente]

    def unisci_cluster(utente1, utente2):
        """Unisce i cluster di due utenti"""
        root1 = trova_root(utente1)
        root2 = trova_root(utente2)
        if root1 != root2:
            utente_a_cluster[root2] = root1

    # Unisci gli utenti che condividono IP
    for utenti_con_stesso_ip in ip_to_users.values():
        if len(utenti_con_stesso_ip) > 1:
            primo = utenti_con_stesso_ip[0]
            for utente in utenti_con_stesso_ip[1:]:
                unisci_cluster(primo, utente)

    # Unisci gli utenti che condividono Device
    for utenti_con_stesso_device in device_to_users.values():
        if len(utenti_con_stesso_device) > 1:
            primo = utenti_con_stesso_device[0]
            for utente in utenti_con_stesso_device[1:]:
                unisci_cluster(primo, utente)

    # Normalizza tutti i cluster (applica path compression a tutti)
    for utente in utente_a_cluster.keys():
        trova_root(utente)

    return utente_a_cluster


def identifica_transazioni_cross_cluster(transazioni, utente_a_cluster):
    """
    Identifica le transazioni che avvengono tra cluster diversi.

    Args:
        transazioni: Lista di transazioni
        utente_a_cluster: Mappa utente -> cluster

    Returns:
        Lista di transazioni cross-cluster (sospette)
    """
    transazioni_sospette = []

    for transazione in transazioni:
        from_user = transazione["from"]
        to_user = transazione["to"]

        cluster_from = utente_a_cluster[from_user]
        cluster_to = utente_a_cluster[to_user]

        # Se i cluster sono diversi, è una transazione cross-cluster
        if cluster_from != cluster_to:
            transazioni_sospette.append({
                **transazione,
                "cluster_from": cluster_from,
                "cluster_to": cluster_to
            })

    return transazioni_sospette


def genera_report(utenti_metadata, transazioni):
    """
    Genera un report completo sull'analisi delle Super-Identità e transazioni sospette.

    Returns:
        Lista di stringhe con il report
    """
    linee = []

    # Trova le Super-Identità
    utente_a_cluster = trova_super_identita(utenti_metadata)

    # Raggruppa gli utenti per cluster
    cluster_to_utenti = {}
    for utente, cluster in utente_a_cluster.items():
        if cluster not in cluster_to_utenti:
            cluster_to_utenti[cluster] = []
        cluster_to_utenti[cluster].append(utente)

    linee.append("=" * 80)
    linee.append("ANALISI SYBIL RING - SUPER-IDENTITÀ")
    linee.append("=" * 80)

    linee.append(f"\nTotale utenti: {len(utenti_metadata)}")
    linee.append(f"Totale Super-Identità trovate: {len(cluster_to_utenti)}")

    linee.append("\n--- DETTAGLIO SUPER-IDENTITÀ ---")
    for i, (cluster_id, utenti) in enumerate(cluster_to_utenti.items(), 1):
        linee.append(f"\nSuper-Identità #{i} (ID: {cluster_id}):")
        linee.append(f"  Utenti: {', '.join(sorted(utenti))}")

        # Mostra IP e Device condivisi
        all_ips = set()
        all_devices = set()
        for utente in utenti:
            all_ips.update(utenti_metadata[utente]["ip"])
            all_devices.update(utenti_metadata[utente]["device_id"])

        linee.append(f"  IP totali: {all_ips}")
        linee.append(f"  Device totali: {all_devices}")

    # Identifica transazioni cross-cluster
    transazioni_sospette = identifica_transazioni_cross_cluster(transazioni, utente_a_cluster)

    linee.append("\n" + "=" * 80)
    linee.append("TRANSAZIONI CROSS-CLUSTER (SOSPETTE)")
    linee.append("=" * 80)

    if transazioni_sospette:
        linee.append(f"\nTrovate {len(transazioni_sospette)} transazioni sospette:\n")
        for trans in transazioni_sospette:
            linee.append(f"⚠️  {trans['from']} → {trans['to']}: {trans['amount']}€")
            linee.append(f"   Da Super-Identità: {trans['cluster_from']}")
            linee.append(f"   A Super-Identità: {trans['cluster_to']}")
            linee.append("")
    else:
        linee.append("\nNessuna transazione cross-cluster trovata.")

    # Calcola totale transazioni interne vs sospette
    transazioni_interne = len(transazioni) - len(transazioni_sospette)
    linee.append(f"\nRIEPILOGO:")
    linee.append(f"  Transazioni totali: {len(transazioni)}")
    linee.append(f"  Transazioni interne al cluster: {transazioni_interne}")
    linee.append(f"  Transazioni cross-cluster (sospette): {len(transazioni_sospette)}")

    if transazioni_sospette:
        totale_sospetto = sum(t["amount"] for t in transazioni_sospette)
        linee.append(f"  Valore totale transazioni sospette: {totale_sospetto}€")

    return linee


if __name__ == "__main__":
    utenti_metadata = {
        "user_01": {"ip": {"192.168.1.10", "10.0.0.1"}, "device_id": {"dev_A", "dev_B"}},
        "user_02": {"ip": {"192.168.1.10"}, "device_id": {"dev_C"}},  # Condivide IP con user_01
        "user_03": {"ip": {"10.0.0.5"}, "device_id": {"dev_B"}},      # Condivide Device con user_01
        "user_04": {"ip": {"172.16.0.1"}, "device_id": {"dev_D"}},
        "user_05": {"ip": {"172.16.0.1"}, "device_id": {"dev_E"}},    # Condivide IP con user_04
        "user_06": {"ip": {"10.0.0.99"}, "device_id": {"dev_F"}},     # Isolato
        "user_07": {"ip": {"192.168.1.20"}, "device_id": {"dev_G"}},
        "user_08": {"ip": {"192.168.1.20"}, "device_id": {"dev_H"}},  # Condivide IP con user_07
    }

    transazioni = [
        {"from": "user_01", "to": "user_02", "amount": 500},    # Interna al cluster (01-02-03)
        {"from": "user_02", "to": "user_03", "amount": 1500},   # Interna
        {"from": "user_03", "to": "user_04", "amount": 8000},   # Sospetta: Tra cluster diversi (01-02-03 -> 04-05)
        {"from": "user_04", "to": "user_05", "amount": 200},    # Interna
        {"from": "user_06", "to": "user_01", "amount": 50},     # Sospetta: Isolato -> Cluster
        {"from": "user_07", "to": "user_08", "amount": 1000},   # Interna
    ]

    report = genera_report(utenti_metadata, transazioni)
    for linea in report:
        print(linea)
