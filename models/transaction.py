# models/transaction.py
from dataclasses import dataclass
from typing import Literal

@dataclass
class Transaction:
    date: str
    description: str
    category: str
    amount: float
    kind: Literal["income", "expense"]