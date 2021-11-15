import pytest
from wallet import Wallet


@pytest.fixture
def my_wallet():
    """Returns a Wallet instance with a zero balance"""
    return Wallet()


@pytest.mark.parametrize("earned,spent,expected", [(30, 10, 20), (20, 2, 18)])
def test_transactions(my_wallet, earned, spent, expected):
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected


# Reference:
# Testing Python Applications with Pytest, semaphoreci.com
