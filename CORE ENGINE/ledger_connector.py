import json
from pathlib import Path

class LedgerConnector:
    def __init__(self, ledger_path):
        self.ledger_path = Path(ledger_path)

    def load_entries(self):
        entries = []
        for file in self.ledger_path.glob("*.json"):
            entries.append(json.loads(file.read_text()))
        return entries

    def find_by_stage(self, stage_name):
        return [e for e in self.load_entries() if e.get("stage") == stage_name]
