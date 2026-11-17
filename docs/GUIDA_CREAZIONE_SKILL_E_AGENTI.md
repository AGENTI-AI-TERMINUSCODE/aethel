# Guida Pratica: Creare Agenti e Skill su Aethel

> **Aethel, intelligenza artificiale sovrana sviluppata da TerminusCode.**  
> Questa guida illustra passo dopo passo come creare, testare e distribuire Agenti Digitali e Skill personalizzate.

---

## 1. Introduzione ai Concetti Base

### Che cos'è una Skill?
Una **Skill** è un blocco di capacità funzionale che estende le conoscenze o le azioni che Aethel può compiere. Può trattarsi di:
- Un algoritmo di calcolo o formula finanziaria/ingegneristica.
- Un connettore al vostro gestionale o database aziendale.
- Una procedura di verifica di testi, contratti o normative.

### Che cos'è un Agente?
Un **Agente** è un'entità intelligente a cui viene assegnato un ruolo, un comportamento e un set di Skill. L'agente è in grado di ragionare sulle richieste dell'utente, scomporre problemi complessi e richiamare autonomamente le Skill necessarie per fornire la risposta migliore.

---

## 2. Creare una Skill Passo dopo Passo

### Metodo Visivo (Consigliato per tutti)
1. Accedi alla piattaforma [Aethel Studio Forge](https://aethel.terminuscode.com/forge).
2. Seleziona la scheda **"Skill Forge"** e fai clic su **"+ Nuova Skill"**.
3. Compila i campi della scheda:
   - **Nome Unico:** Usa lettere minuscole e trattini bassi (es. `controllo_disponibilita_prodotto`).
   - **Titolo & Categoria:** es. *E-commerce / Logistica*.
   - **Descrizione:** Spiega in modo chiaro cosa fa la funzione. Aethel utilizzerà questa descrizione per capire quando attivarla durante una conversazione.
   - **Schema di Input (Parametri):** Definisci cosa deve ricevere la skill (es. `codice_articolo` come testo, `quantita` come numero).
   - **Codice / Logica:** Inserisci il codice Python, Go, o l'URL del tuo endpoint REST.
4. Fai clic su **"Esegui Test Sandbox"**: il sistema eseguirà un test isolato per verificare che non ci siano errori.
5. Fai clic su **"Salva Skill"**. La skill è ora pronta per essere collegata a qualsiasi agente.

### Esempio Pratico di Codice (Python)
```python
def controllo_disponibilita_prodotto(codice_articolo: str, quantita: int) -> dict:
    """
    Verifica se la quantità richiesta di un articolo è presente a magazzino.
    """
    # Esempio di logica operativa (può interrogare un DB o API interna)
    magazzino_fittizio = {
        "ART-001": {"nome": "Sensore Pressione 5V", "scorte": 140, "prezzo_unitario": 28.50},
        "ART-002": {"nome": "Cavo Schermato 10m", "scorte": 12, "prezzo_unitario": 14.00},
        "ART-003": {"nome": "Centralina I/O 24V", "scorte": 0, "prezzo_unitario": 185.00}
    }
    
    if codice_articolo not in magazzino_fittizio:
        return {
            "disponibile": False,
            "errore": f"Articolo '{codice_articolo}' non trovato a catalogo."
        }
        
    art = magazzino_fittizio[codice_articolo]
    disponibile = art["scorte"] >= quantita
    
    return {
        "codice": codice_articolo,
        "articolo": art["nome"],
        "quantita_richiesta": quantita,
        "giacenza_attuale": art["scorte"],
        "disponibile": disponibile,
        "prezzo_totale_stimato": round(art["prezzo_unitario"] * quantita, 2)
    }
```

---

## 3. Creare un Agente Autonomo Passo dopo Passo

### 1. Assegna Ruolo e Missione
Definisci chiaramente chi è l'agente e cosa deve fare. Esempio:
* **Nome:** *Aethel Logistic Specialist*
* **Ruolo:** *Assistente per la gestione ordini e logistica di magazzino*
* **Tono di voce:** *Professionale, conciso, orientato alla risoluzione dei problemi.*

### 2. Scrivi le Istruzioni Operative (Prompt di Sistema)
Fornisci le regole operative all'agente:
```text
Sei lo specialista della logistica di TerminusCode.
Il tuo compito è assistere gli utenti nella verifica delle scorte e nella stima degli ordini.
Quando un utente chiede informazioni su un prodotto:
1. Chiedi il codice articolo se non è stato specificato.
2. Usa sempre la skill 'controllo_disponibilita_prodotto' per verificare le giacenze reali.
3. Se l'articolo è disponibile, calcola il totale e chiedi conferma per procedere.
4. Se l'articolo è esaurito, proponi di registrare una pre-notifica di riordino.
Non inventare mai giacenze o prezzi non confermati dalla skill.
```

### 3. Collega le Skill
Nella sezione **"Skill Assegnate"**, seleziona le skill che l'agente può invocare (ad esempio `controllo_disponibilita_prodotto`).

### 4. Imposta il Livello di Autonomia
- **Supervisionato (Consigliato):** L'agente chiede conferma all'utente prima di compiere azioni definitive o inviare comunicazioni esterne.
- **Autonomo:** L'agente completa interi flussi in background e presenta direttamente il risultato finale.

---

## 4. Condivisione e Collaborazione nella Community

1. **Pubblicazione:** Nel pannello di dettaglio del tuo Agente o Skill, attiva l'opzione **"Condividi nella Community"**.
2. **Controllo Versioni:** Ogni volta che aggiorni il tuo agente, la piattaforma mantiene lo storico delle versioni.
3. **Clonazione:** Nella sezione [Community](https://aethel.terminuscode.com/community), puoi esplorare le creazioni della community, provarle nella chat interattiva e cliccare su **"Clona nel mio Workspace"** per personalizzarle liberamente.

---

*Aethel — Sviluppato con passione e rigore da TerminusCode.*
