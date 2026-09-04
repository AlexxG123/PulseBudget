from dataclasses import dataclass, asdict

@dataclass
class Transaction:
    """Represents an income or expense transaction in the system."""
    id: int
    date: str
    description: str
    category: str
    amount: float
    kind: str  # 'Income' or 'Expense'

    def to_dict(self) -> dict:
        """Converts the transaction to a dictionary for JSON storage."""
        return asdict(self)