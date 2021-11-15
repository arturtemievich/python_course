# Basic Pytest Usage
# Pytest expects our tests to be located in files whose names begin with test_ or end with _test.py

import pytest
from wallet import Wallet


def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0


def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100


def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100


def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10

# You may have noticed some repetition in the way we initialized the class in each test.
# This is where pytest 'fixtures' come in. Refactoring our Tests with Fixtures.

# @pytest.fixture
# def empty_wallet():
#     """Returns a Wallet instance with a zero balance"""
#     return Wallet()
#
#
# @pytest.fixture
# def wallet():
#     """Returns a Wallet instance with a balance of 20"""
#     return Wallet(20)
#
#
# def test_default_initial_amount(empty_wallet):
#     assert empty_wallet.balance == 0
#
#
# def test_setting_initial_amount(wallet):
#     assert wallet.balance == 20
#
#
# def test_wallet_add_cash(wallet):
#     wallet.add_cash(80)
#     assert wallet.balance == 100
#
#
# def test_wallet_spend_cash(wallet):
#     wallet.spend_cash(10)
#     assert wallet.balance == 10

# In our refactored tests, we can see that we have reduced the amount of boilerplate code by making use of fixtures.
# We define two fixture functions, wallet and empty_wallet,
# which will be responsible for initializing the Wallet class in tests where it is needed, with different values.

# CONCLUSION: Utilizing fixtures helps us de-duplicate our code.
# If you notice a case where a piece of code is used repeatedly in a number of tests,
# that might be a good candidate to use as a fixture.

# It is a good practice to add docstrings for your fixtures.
# To see all the available fixtures, run the following command:
# pytest --fixtures
