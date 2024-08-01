import pytest
import sys
sys.path.append('../')

from application.financial_operation_processor import FOP, Account, Debit


def test_account_initialization():
    fop = FOP()
    account_data = {
        "client_id": 123,
        "active_card": True,
        "available_limit": 1000
    }
    account = Account(account_data)
    account.process(fop)
    assert fop.account.client_id == 123
    assert fop.account.active_card is True
    assert fop.account.available_limit == 1000

if __name__ == '__main__':
    pytest.main()
