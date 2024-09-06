import pytest

from design_pytterns.behavioral.observer import (
    Counter,
    DoubleCounter,
    Subject,
)


@pytest.fixture(
    params=(
        {"results": {"counter": 1, "double_counter": 2}},
        {"start": 1, "results": {"counter": 2, "double_counter": 3}},
        {"increment": 2, "results": {"counter": 2, "double_counter": 4}},
        {"start": 5, "increment": 10, "results": {"counter": 15, "double_counter": 25}},
    ),
    ids=("default_values", "set_start", "set_increment", "set_start_and_increment"),
)
def fixture_value(request):
    results = request.param.pop("results")

    subject = Subject()

    counter = Counter(**request.param)
    subject.register_observer(counter)

    double_counter = DoubleCounter(**request.param)
    subject.register_observer(double_counter)

    return subject, counter, double_counter, results


def test_observers(fixture_value):
    subject, counter, double_counter, results = fixture_value

    print(counter.__dict__)

    subject.notify_observers()
    assert counter.value == results["counter"]
    assert double_counter.value == results["double_counter"]
