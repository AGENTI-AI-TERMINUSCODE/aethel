"""
Esempio di Skill Aethel in Python
Calcolo del preventivo con sconti dinamici e verifica di convenienza.
"""

def calcola_preventivo(importo_base: float, volume_articoli: int, cliente_premium: bool = False) -> dict:
    """
    Calcola l'importo scontato in base al volume di acquisto e allo status del cliente.
    """
    sconto_volume = 0.0
    if volume_articoli >= 100:
        sconto_volume = 15.0
    elif volume_articoli >= 50:
        sconto_volume = 10.0
    elif volume_articoli >= 20:
        sconto_volume = 5.0

    sconto_status = 5.0 if cliente_premium else 0.0
    sconto_totale_percentuale = min(sconto_volume + sconto_status, 25.0)

    valore_sconto = (importo_base * sconto_totale_percentuale) / 100.0
    totale_scontato = importo_base - valore_sconto

    return {
        "importo_base": importo_base,
        "volume_articoli": volume_articoli,
        "cliente_premium": cliente_premium,
        "sconto_percentuale_applicato": sconto_totale_percentuale,
        "totale_risparmiato": round(valore_sconto, 2),
        "totale_finale": round(totale_scontato, 2)
    }

if __name__ == "__main__":
    risultato = calcola_preventivo(1250.00, 60, cliente_premium=True)
    print("Risultato Test Preventivo:", risultato)
