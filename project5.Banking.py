# ===== Starter Template: Mini Banking System =====
from __future__ import annotations
from datetime import date
from typing import Dict, list, tuple

Txn = tuple[str, str, float, float] # (iso_date, type, amount, balance_after)
class Account:
    def __init__(self, account_id : str, owner : str):
        self.account_id = account_id
        self.owner = owner
        self._balance: float = 0.0
        self._history = list[Txn] = []
        
    def _record(self, typ: str, amount: float) -> None:
     # TODO : append transction(date, typ, amount, balance_after)
     raise NotImplementedError
    
    def deposit(self, amount: float) ->None:
     # TODO : validate amount > 0 , update balance, record
     raise NotImplementedError
 
    def get_balance(self) ->float:
        return self._balance
    
    def _set_balance(self, new_balance: float) -> None:
     self.__balance = new_balance
     
    def withdraw(self, amount: float) -> None:
     # TODO: overridden in subclasses
     raise NotImplementedError
 
    def transfer(self, to: "Account", amount: float) -> None:
    # TODO: validate not same account + amount > 0
    # TODO: withdraw then deposit (atomic)
     raise NotImplementedError
 
    def statement(self) -> list[Txn]: # type: ignore
     return list(self._history) 
  
class CurrentAccount(Account):
    def __init__(self, account_id: str, owner: str, overdraft_limit: float = 5000.0):
     super().__init__(account_id, owner)
     self.overdraft_limit = overdraft_limit
     
    def withdraw(self, amount: float) -> None:
     # TODO: allow negative balance down to -overdraft_limit
     raise NotImplementedError

class Bank:
    def __init__(self):
        self.accounts = Dict[str, Account] = {}
        
    def open_account(self, account: Account) -> None:
     # TODO: unique ID check, then store
     raise NotImplementedError
 
    def get_account(self, account_id: str) -> Account:
     # TODO: return account or raise KeyError
     raise NotImplementedError
 
    def transfer(self, from_id: str, to_id: str, amount: float) -> None:
     # TODO: lookup accounts, then call transfer
     raise NotImplementedError