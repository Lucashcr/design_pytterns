from abc import ABC, abstractmethod
from decimal import Decimal


class Strategy(ABC):
    def __init__(
        self, amount: float, rate: float, time: float, decimal_places: int = 2
    ):
        self.amount = Decimal(amount)
        self.rate = Decimal(rate)
        self.time = Decimal(time)
        self.__exp = Decimal(10) ** -decimal_places

    @abstractmethod
    def calculate_interest(self) -> Decimal: ...

    @abstractmethod
    def calculate_final_amount(self) -> Decimal: ...

    @property
    def interest(self) -> float:
        return float(self.calculate_interest().quantize(Decimal(self.__exp)))

    @property
    def final_amount(self) -> float:
        return float(self.calculate_final_amount().quantize(Decimal(self.__exp)))
