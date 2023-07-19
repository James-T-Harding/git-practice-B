## Intermediate Challenges
### ex 5:
```Python
from collections import Counter

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
duplicates = [key for key, value in Counter(sample_list).items() if value >= 2]

print(duplicates)
```

### ex 6:
```Python
# Dictionary
d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}

# Filter dict using following keys
l1 = ['A', 'C', 'F']

new_dict = {key: d1[key] for key in l1}
print(new_dict)
```

### ex 7:
```Python
# Dictionary
for n in range(1, 6):
    stars = (6-n) * [n]
    print(*stars)
```


## Code Wars
https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python

Create a function taking a positive integer between 1 and 3999 
(both included) as its parameter and returning a string containing 
the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately 
starting with the left most digit and skipping any digit with a value of zero. 
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 
2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses 
each Roman symbol in descending order: MDCLXVI.

This one took a while...I ended up having to use some things we hadn't _strictly_ covered yet.

```Python
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
```

After looking at the most upvoted solution, I discovered there _are_ simpler solutions, but it isn't immediately obvious.
