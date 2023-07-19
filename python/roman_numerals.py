from dataclasses import dataclass


@dataclass
class Converter:
    low: str
    med: str = None
    high: str = None

    def convert(self, value):
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


def solution(n):
    th = int(n / 1000)
    hun = int(n % 1000 / 100)
    ten = int(n % 100 / 10)
    di = n % 10

    return thousands.convert(th) + hundreds.convert(hun) + tens.convert(ten) + digits.convert(di)


def solutionB(n):
    roman_numerals = [
      (1000, 'M'),
      (900, 'CM'),
      (500, 'D'),
      (400, 'CD'),
      (100, 'C'),
      (90, 'XC'),
      (50, 'L'),
      (40, 'XL'),
      (10, 'X'),
      (9, 'IX'),
      (5, 'V'),
      (4, 'IV'),
      (1, 'I')
    ]

    roman_string = ''
    for value, symbol in roman_numerals:
        while n >= value:
            roman_string += symbol
            n -= value
    return roman_string


