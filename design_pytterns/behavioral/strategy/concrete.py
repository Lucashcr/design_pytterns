from decimal import Decimal
from .strategy import Strategy


class SimpleInterestStrategy(Strategy):
    def calculate_interest(self) -> float:
        return self.amount * self.rate * self.time

    def calculate_final_amount(self) -> float:
        return self.amount + self.interest


class CompoundInterestStrategy(Strategy):
    def calculate_interest(self) -> float:
        return self.final_amount - self.amount

    def calculate_final_amount(self) -> float:
        return self.amount * (1 + self.rate) ** self.time
