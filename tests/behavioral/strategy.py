import pytest

from design_pytterns.behavioral.strategy import (
    CompoundInterestStrategy,
    InterestContext,
    SimpleInterestStrategy,
)

from design_pytterns.behavioral.strategy.strategy import Strategy


@pytest.mark.parametrize(
    "amount, rate, time, expected",
    [
        (1000, 0.05, 1, 50),
        (1000, 0.05, 2, 100),
        (1000, 0.05, 3, 150),
    ],
)
def test_simple_interest_strategy(amount, rate, time, expected):
    strategy = SimpleInterestStrategy(amount, rate, time)

    context = InterestContext(strategy)
    assert context.interest == expected


@pytest.mark.parametrize(
    "amount, rate, time, expected",
    [
        (1000, 0.05, 1, 1050),
        (1000, 0.05, 2, 1102.5),
        (1000, 0.05, 3, 1157.63),
    ],
)
def test_compound_interest_strategy_final_amount(amount, rate, time, expected):
    strategy = CompoundInterestStrategy(amount, rate, time)

    context = InterestContext(strategy)
    assert context.final_amount == expected
