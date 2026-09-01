# services/data_service.py
from models.transaction import Transaction
from typing import List

class DataService:
    """In-memory storage for transactions. (No database)"""
    def __init__(self):
        self.transactions: List[Transaction] = []

    def add(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)

    def get_all(self) -> List[Transaction]:
        return self.transactions