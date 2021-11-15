import pytest
from wallet import Wallet


@pytest.mark.parametrize("earned, spent, expected", [(30, 10, 20), (20, 2, 18)])  # add: (20, 2, 20)
def test_transactions(earned, spent, expected):
    my_wallet = Wallet()
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected
