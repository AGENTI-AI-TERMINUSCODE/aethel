# Contribuire all'Ecosistema Aethel

Grazie per il tuo interesse nel contribuire alla community di **Aethel by TerminusCode**!

## Come Puoi Contribuire

1. **Condividi Skill & Agenti nella Community:**  
   Crea e testa le tue Skill o i tuoi Agenti su [Aethel Studio Forge](https://aethel.terminuscode.com/forge) e pubblicali nel [Community Hub](https://aethel.terminuscode.com/it/community) così che altri sviluppatori e aziende possano clonarli con un clic.
2. **Proponi Template ed Esempi in questo Repository:**  
   Puoi inviare Pull Request con nuovi esempi pratici nella cartella `examples/` (Python, Go, configurazioni JSON di Agenti, integrazioni Webhook).
3. **Migliora Documentazione & Casi d'Uso:**  
   Segnala chiarimenti utili, guide verticali o scenari reali di adozione tramite GitHub Issues.

## Linee Guida di Qualità per le Skill di Esempio

* Ogni Skill Python deve esporre chiaramente il punto di ingresso `def run(args: dict) -> dict:`.
* Includi sempre una breve docstring chiara, gestione pulita degli input mancanti e un risultato JSON leggibile.
* **Non includere mai** API key reali, password, token o dati personali reali negli esempi.
