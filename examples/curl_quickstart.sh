#!/usr/bin/env bash
# Aethel by TerminusCode — Quickstart REST API per Skill e Agenti Sovrani
set -euo pipefail

BASE_URL="https://aethel.terminuscode.com"

echo "1. Verifica catalogo Skill disponibili..."
curl -s "${BASE_URL}/api/v1/skills/list" | head -c 300
echo -e "
"

echo "2. Registrazione Skill di esempio (calcolo IVA e totale)..."
CREATE_RES=$(curl -s -X POST "${BASE_URL}/api/v1/forge/skills"   -H "Content-Type: application/json"   -d '{
    "name": "esempio_calcolo_iva_cli",
    "description": "Calcola imponibile, IVA 22% e totale documento",
    "runtime": "python_jit",
    "execution_code": "def run(args):
    imp = float(args.get("importo_netto", 0))
    aliq = float(args.get("aliquota", 22))
    iva = round(imp * aliq / 100.0, 2)
    return {"imponibile": imp, "aliquota": aliq, "iva": iva, "totale": round(imp + iva, 2)}",
    "timeout_ms": 2000,
    "max_memory_mb": 128,
    "author": "Enterprise Developer"
  }')
echo "${CREATE_RES}"
echo ""

echo "3. Esecuzione Skill in sandbox isolata..."
curl -s -X POST "${BASE_URL}/api/v1/forge/skills/run"   -H "Content-Type: application/json"   -d '{
    "skill_id": "esempio_calcolo_iva_cli",
    "parameters": { "importo_netto": 2500.0, "aliquota": 22 }
  }'
echo ""
