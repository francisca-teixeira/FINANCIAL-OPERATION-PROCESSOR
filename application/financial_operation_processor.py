#!/usr/bin/env python3

import sys
import json
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
import os
from decimal import Decimal


class MyEncoder(json.JSONEncoder):
    def encode(self, obj):
        if isinstance(obj, float) or isinstance(obj, Decimal):
            return format(obj, '.2f')

        if isinstance(obj, dict) and len(obj) > 0:
            result = '{'
            for key, value in obj.items():
                encoded_value = self.encode(value)
                result += f'"{key}": {encoded_value}, '
            result = result[:-2] + '}'
            return result

        if isinstance(obj, list) and len(obj) > 0:
            result = '['
            for value in obj:
                encoded_value = self.encode(value)
                result += encoded_value + ', '
            result = result[:-2] + ']'
            return result

        return json.JSONEncoder.encode(self, obj)


class FOP:
    def __init__(self) -> None:
        self.violations = []
        self.operations = []
        self.last_two_minutes = []
        self.account = None
        try:
            self.file = open(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                + '/output/output', 'w')
        except FileNotFoundError:
            self.file = open('output.json', 'w')

    def read_operations(self):
        """
        Reads json file from stdin
        """
        for line in sys.stdin:
            operation = json.loads(line)
            if "account" in operation:
                self.operations.append(Account(operation["account"]))
            elif "debit" in operation:
                self.operations.append(Debit(operation["debit"]))

    def process_operations(self):
        """
        Loops through the operations and processes them
        """
        self.read_operations()
        for operation in self.operations:
            self.violations.clear()
            operation.process(self)
        self.file.close()

    @staticmethod
    def format_decimal(value):
        return Decimal(value).quantize(Decimal('0.00'))

    def print_output(self):
        if not self.account:
            output = {
                "account": {
                    "client_id": 0,
                    "active_card": "false",
                    "available_limit": 0.00},
                "violations": ["account-not-initialized"]
            }
        else:
            output = {
                "account": {
                    "client_id": self.account.client_id,
                    "active_card": self.account.active_card,
                    "available_limit":
                    FOP.format_decimal(self.account.available_limit)
                } if self.account else None, "violations": self.violations
            }
        self.file.write(json.dumps(output, cls=MyEncoder) + '\n')
        print(json.dumps(output, cls=MyEncoder))
        sys.stdout.flush()


class Operation(ABC):
    @abstractmethod
    def process(self, fop):
        pass


class Account(Operation):
    def __init__(self, account):
        self.client_id = account["client_id"]
        self.active_card = account["active_card"]
        self.available_limit = Decimal(account["available_limit"])

    def process(self, fop):
        """
        Checks all the requirements for the account creation operation
        and creates it if everything is fine.
        """
        if fop.account:
            fop.violations.append("account-already-initialized")
        else:
            fop.account = self
        fop.print_output()


class Debit(Operation):
    def __init__(self, debit):
        self.client_id = debit["client_id"]
        self.merchant = debit["merchant"]
        self.amount = Decimal(debit["amount"])
        self.time = datetime.strptime(debit["time"], "%Y-%m-%dT%H:%M:%S.%fZ")

    def process(self, fop):
        """
        Checks all the requirements for the debit operation and if
        everything is alright, executes the debit.
        """
        if not fop.account:
            fop.violations.append("account-not-initialized")
        elif not fop.account.active_card:
            fop.violations.append("card-not-active")
        elif fop.account.available_limit < self.amount:
            fop.violations.append("insufficient-limit")
        else:
            self._check_high_frequency(fop)
            self._check_doubled_transaction(fop)

        if not fop.violations:
            fop.account.available_limit -= self.amount
            fop.last_two_minutes.append(self)
        fop.print_output()

    def _check_high_frequency(self, fop):
        """
        Checks if there is more than 3 transactions in the last 2 minutes.
        """
        now = self.time
        recent_transactions = [tx for tx in fop.last_two_minutes
                               if now - tx.time < timedelta(minutes=2)]
        if len(recent_transactions) >= 3:
            fop.violations.append("high-frequency-small-interval")

    def _check_doubled_transaction(self, fop):
        """
        Checks if there is 2 transactions in the last 2 minutes from the
        same merchant.
        """
        now = self.time
        for tx in fop.last_two_minutes:
            if (now - tx.time < timedelta(minutes=2)
                and tx.merchant == self.merchant
                    and tx.amount == self.amount):
                fop.violations.append("doubled-transaction")
                break


if __name__ == "__main__":
    fop = FOP()
    fop.process_operations()
