# Customer Integration Platform

Level: 16 — FDE / Customer Engineering

Skills: Python, webhook and mapping gates

Pass when mapping and sandbox_ok are true. Writes to the customer ledger are refused via applied false.

```bash
pip install -r requirements.txt
pytest -q
```

This is a local laptop proof. It does not call a hosted model and it does not apply production changes.
