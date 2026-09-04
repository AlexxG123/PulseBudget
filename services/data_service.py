import json
import os
from typing import List, Dict
from models.transaction import Transaction

class DataService:
    """Manages transactions with local JSON persistence."""
    FILE_PATH = "data.json"

    def __init__(self):
        self._transactions: List[Transaction] = []
        self._next_id: int = 1
        self._load_from_file()

    def _load_from_file(self):
        """Loads transactions from the local JSON file if it exists."""
        if os.path.exists(self.FILE_PATH):
            try:
                with open(self.FILE_PATH, "r", encoding="utf-8") as f:
                    raw_data = json.load(f)
                    for item in raw_data:
                        t = Transaction(**item)
                        self._transactions.append(t)
                    if self._transactions:
                        self._next_id = max(t.id for t in self._transactions) + 1
            except Exception:
                self._transactions = []

    def _save_to_file(self):
        """Saves current transactions to the local JSON file."""
        with open(self.FILE_PATH, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self._transactions], f, indent=4)

    def add_transaction(self, date: str, description: str, category: str, amount: float, kind: str) -> Transaction:
        """Creates, adds and persists a new transaction."""
        transaction = Transaction(
            id=self._next_id,
            date=date,
            description=description,
            category=category,
            amount=amount,
            kind=kind
        )
        self._transactions.append(transaction)
        self._next_id += 1
        self._save_to_file()
        return transaction

    def delete_transaction(self, transaction_id: int) -> bool:
        """Deletes a transaction by ID and updates the JSON file."""
        initial_len = len(self._transactions)
        self._transactions = [t for t in self._transactions if t.id != transaction_id]
        if len(self._transactions) < initial_len:
            self._save_to_file()
            return True
        return False

    def get_filtered_transactions(self, kind_filter: str = "All") -> List[Transaction]:
        """Returns transactions filtered by kind."""
        if kind_filter == "All":
            return self._transactions
        return [t for t in self._transactions if t.kind.lower() == kind_filter.lower()]

    def calculate_totals(self) -> Dict[str, float]:
        """Calculates total income, total expense, and net balance."""
        income = sum(t.amount for t in self._transactions if t.kind.lower() == "income")
        expense = sum(t.amount for t in self._transactions if t.kind.lower() == "expense")
        return {
            "income": income,
            "expense": expense,
            "balance": income - expense
        }

    def get_category_breakdown(self) -> Dict[str, float]:
        """Calculates expense percentages per category."""
        totals = self.calculate_totals()
        total_expense = totals["expense"]
        if total_expense == 0:
            return {}

        breakdown = {}
        for t in self._transactions:
            if t.kind.lower() == "expense":
                breakdown[t.category] = breakdown.get(t.category, 0) + t.amount

        # Convert to relative percentages (0.0 to 1.0)
        return {cat: amt / total_expense for cat, amt in breakdown.items()}
    def get_financial_health(self) -> dict:
        """Calculates a health score (0-100) and provides smart insights."""
        totals = self.calculate_totals()
        income = totals["income"]
        expense = totals["expense"]

        if income == 0:
            return {
                "score": 50,
                "status": "Neutral",
                "color": "#8A9BB4",
                "advice": "Add your monthly income to unlock smart insights."
            }

        savings_rate = ((income - expense) / income) * 100

        if savings_rate >= 30:
            return {
                "score": 95,
                "status": "Excellent",
                "color": "#4ADE80",
                "advice": f"Great job! You are saving {savings_rate:.1f}% of your income."
            }
        elif savings_rate > 0:
            return {
                "score": 70,
                "status": "Good",
                "color": "#22D3EE",
                "advice": f"You are saving {savings_rate:.1f}%. Try cutting non-essential expenses."
            }
        else:
            return {
                "score": 30,
                "status": "Warning",
                "color": "#FB7185",
                "advice": "Alert: Expenses exceed income! Review your breakdown below."
            }