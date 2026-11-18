# Aethel Sovereign Python SDK

```python
from aethel_sdk import AethelClient

client = AethelClient(api_key="YOUR_API_KEY")
res = client.chat([{"role": "user", "content": "Confronta Redis e PostgreSQL"}])
print(res["choices"][0]["message"]["content"])

# Deterministic CSV analysis & binary .xlsx export
stats = client.data_analyst("mese,ricavi\nGen,18500\nFeb,21400", "sales.csv")
client.export_binary("xlsx", "Report_Q1", stats["markdown"], out_path="report.xlsx")
```
