const API_URL = "https://aethel.terminuscode.com/api/query";
const sessionId = "ext_" + Date.now();
const messagesEl = document.getElementById("messages");
const formEl = document.getElementById("chatForm");
const inputEl = document.getElementById("promptInput");
const btnSummarize = document.getElementById("btnSummarize");

function addMsg(role, text) {
  const d = document.createElement("div");
  d.className = "msg " + role;
  d.textContent = text;
  messagesEl.appendChild(d);
  messagesEl.scrollTop = messagesEl.scrollHeight;
  return d;
}

async function askAethel(query) {
  addMsg("user", query.length > 260 ? query.slice(0, 260) + "..." : query);
  const placeholder = addMsg("assistant", "Elaborazione in corso...");
  try {
    const r = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json", "X-User-ID": sessionId },
      body: JSON.stringify({ query, session_id: sessionId, language: navigator.language.slice(0, 2) || "it", history: [] })
    });
    const data = await r.json();
    placeholder.textContent = data.final_answer || data.response || "Nessuna risposta ricevuta.";
  } catch (err) {
    placeholder.textContent = "Errore di connessione ad Aethel: " + err.message;
  }
}

formEl.addEventListener("submit", (e) => {
  e.preventDefault();
  const q = inputEl.value.trim();
  if (!q) return;
  inputEl.value = "";
  askAethel(q);
});

btnSummarize.addEventListener("click", async () => {
  try {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    const [{ result }] = await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: () => (document.body.innerText || "").slice(0, 3500)
    });
    askAethel(`Riassumi in 5 punti chiave la pagina "${tab.title}":\n\n${result}`);
  } catch (err) {
    addMsg("assistant", "Impossibile leggere questa scheda: " + err.message);
  }
});
