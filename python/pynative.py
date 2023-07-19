from dataclasses import dataclass


@dataclass
class Converter:
    low: str
    med: str = None
    high: str = None

    def convert(self, value):
        output = ""

        if value == 9:
            return self.low + self.high
        if value >= 5:
            diff = value - 5
            return self.med + diff * self.low
        if value == 4:
            return self.low + self.med

        return value * self.low


thousands = Converter('M')
hundreds = Converter('C', 'D', 'M')
tens = Converter('X', 'L', 'C')
digits = Converter('I', 'V', 'X')

converters = [thousands, hundreds, tens, digits]


def solution(n):
    th = int(n / 1000)
    hun = int(n % 1000 / 100)
    ten = int(n % 100 / 10)
    di = n % 10

    answer = thousands.convert(th) + hundreds.convert(hun) + tens.convert(ten) + digits.convert(di)