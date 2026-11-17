"""
Esempio di Skill Aethel in Python (Runtime python_jit)
Calcolo del preventivo con sconti dinamici e verifica di convenienza.
La funzione principale deve essere definita come: def run(args):
"""

def run(args: dict) -> dict:
    """
    Riceve i parametri dal runtime di Aethel e calcola l'importo scontato.
    """
    importo_base = float(args.get("importo_base", 0.0))
    volume_articoli = int(args.get("volume_articoli", 1))
    cliente_premium = bool(args.get("cliente_premium", False))

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
        "status": "CALCOLO_COMPLETATO",
        "importo_base": importo_base,
        "volume_articoli": volume_articoli,
        "cliente_premium": cliente_premium,
        "sconto_percentuale_applicato": sconto_totale_percentuale,
        "totale_risparmiato": round(valore_sconto, 2),
        "totale_finale": round(totale_scontato, 2)
    }

if __name__ == "__main__":
    test_args = {"importo_base": 1250.0, "volume_articoli": 60, "cliente_premium": True}
    print("Test Locale:", run(test_args))
