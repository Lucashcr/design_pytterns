from .strategy import Strategy


class InterestContext:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    @property
    def interest(self):
        return self.strategy.interest

    @property
    def final_amount(self):
        return self.strategy.final_amount
