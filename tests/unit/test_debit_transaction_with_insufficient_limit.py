import pytest
import sys
sys.path.append('../')

from application.financial_operation_processor import FOP, Account, Debit


def test_debit_transaction_with_insufficient_limit():
    fop = FOP()
    account_data = {
        "client_id": 123,
        "active_card": True,
        "available_limit": 100
    }
    account = Account(account_data)
    account.process(fop)

    debit_data = {
        "client_id": 123,
        "merchant": "Shop A",
        "amount": 200,
        "time": "2022-01-01T12:00:00.000Z"
    }
    debit = Debit(debit_data)
    debit.process(fop)

    assert fop.account.available_limit == 100
    assert "insufficient-limit" in fop.violations

if __name__ == "__main__":
    pytest.main()
