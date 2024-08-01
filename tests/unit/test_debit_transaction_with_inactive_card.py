import pytest
import sys
sys.path.append('../')

from application.financial_operation_processor import FOP, Account, Debit


def test_debit_transaction_with_inactive_card():
    fop = FOP()
    account_data = {
        "client_id": 123,
        "active_card": False,
        "available_limit": 1000
    }
    account = Account(account_data)
    account.process(fop)

    debit_data = {
        "client_id": 123,
        "merchant": "Shop A",
        "amount": 100,
        "time": "2022-01-01T12:00:00.000Z"
    }
    debit = Debit(debit_data)
    debit.process(fop)

    assert fop.account.available_limit == 1000
    assert "card-not-active" in fop.violations

if __name__ == "__main__":
    pytest.main()
