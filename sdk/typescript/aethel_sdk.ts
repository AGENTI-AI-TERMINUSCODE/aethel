/**
 * Aethel Sovereign AI — Official TypeScript SDK (v5.0)
 * TerminusCode — https://aethel.terminuscode.com
 */
export interface AethelChatMessage {
  role: "system" | "user" | "assistant";
  content: string;
}

export class AethelClient {
  private baseUrl: string;
  private headers: Record<string, string>;

  constructor(opts: { apiKey?: string; baseUrl?: string; userId?: string } = {}) {
    this.baseUrl = (opts.baseUrl || "https://aethel.terminuscode.com").replace(/\/$/, "");
    this.headers = {
      "Content-Type": "application/json",
      "X-User-ID": opts.userId || "ts_sdk_user",
      ...(opts.apiKey ? { Authorization: `Bearer ${opts.apiKey}` } : {}),
    };
  }

  private async post<T>(path: string, body: unknown): Promise<T> {
    const res = await fetch(`${this.baseUrl}${path}`, {
      method: "POST",
      headers: this.headers,
      body: JSON.stringify(body),
    });
    if (!res.ok) throw new Error(`Aethel API ${res.status}: ${await res.text()}`);
    return res.json() as Promise<T>;
  }

  chat(messages: AethelChatMessage[], model = "aethel-singularity-pro", responseFormat?: Record<string, unknown>) {
    return this.post("/api/v1/chat/completions", { model, messages, stream: false, ...(responseFormat ? { response_format: responseFormat } : {}) });
  }

  dataAnalyst(content: string, filename = "data.csv") {
    return this.post("/api/v1/tools/data_analyst", { filename, content });
  }

  documentDiff(docA: string, docB: string) {
    return this.post("/api/v1/tools/document_diff", { doc_a: docA, doc_b: docB });
  }

  exportBinary(format: "xlsx" | "docx" | "pdf" | "slides", title: string, content: string) {
    return this.post<{ filename: string; mime_type: string; base64_data: string }>("/api/v1/export/document", { format, title, content });
  }

  deepResearch(topic: string, lang = "it") {
    return this.post<{ dossier: string }>("/api/v1/research/dossier", { topic, lang });
  }

  codeSandbox(code: string, language: "python" | "go" = "python") {
    return this.post("/api/v1/tools/code_sandbox", { language, code });
  }
}
