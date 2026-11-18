"""
Aethel Sovereign AI — Official Python SDK (v5.0)
Zero-bloat client for https://aethel.terminuscode.com (TerminusCode)
"""
import base64
import requests
from typing import Any, Dict, List, Optional


class AethelClient:
    def __init__(self, api_key: str = "", base_url: str = "https://aethel.terminuscode.com", user_id: str = "sdk_user", timeout: int = 35):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.headers = {"Content-Type": "application/json", "X-User-ID": user_id}
        if api_key:
            self.headers["Authorization"] = f"Bearer {api_key}"

    def chat(self, messages: List[Dict[str, str]], model: str = "aethel-singularity-pro", response_format: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        payload: Dict[str, Any] = {"model": model, "messages": messages, "stream": False}
        if response_format:
            payload["response_format"] = response_format
        r = requests.post(f"{self.base_url}/api/v1/chat/completions", json=payload, headers=self.headers, timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def data_analyst(self, content: str, filename: str = "data.csv") -> Dict[str, Any]:
        r = requests.post(f"{self.base_url}/api/v1/tools/data_analyst", json={"filename": filename, "content": content}, headers=self.headers, timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def document_diff(self, doc_a: str, doc_b: str) -> Dict[str, Any]:
        r = requests.post(f"{self.base_url}/api/v1/tools/document_diff", json={"doc_a": doc_a, "doc_b": doc_b}, headers=self.headers, timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def export_binary(self, fmt: str, title: str, content: str, out_path: Optional[str] = None) -> Dict[str, Any]:
        """fmt: 'xlsx' | 'docx' | 'pdf' | 'slides'"""
        r = requests.post(f"{self.base_url}/api/v1/export/document", json={"format": fmt, "title": title, "content": content}, headers=self.headers, timeout=self.timeout)
        r.raise_for_status()
        data = r.json()
        if out_path and data.get("base64_data"):
            with open(out_path, "wb") as f:
                f.write(base64.b64decode(data["base64_data"]))
        return data

    def deep_research(self, topic: str, lang: str = "it") -> Dict[str, Any]:
        r = requests.post(f"{self.base_url}/api/v1/research/dossier", json={"topic": topic, "lang": lang}, headers=self.headers, timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def code_sandbox(self, code: str, language: str = "python") -> Dict[str, Any]:
        r = requests.post(f"{self.base_url}/api/v1/tools/code_sandbox", json={"language": language, "code": code}, headers=self.headers, timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def sla_status(self) -> Dict[str, Any]:
        r = requests.get(f"{self.base_url}/api/v1/status/sla", timeout=10)
        r.raise_for_status()
        return r.json()
