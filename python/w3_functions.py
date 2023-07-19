import math
# I know 1-3 have inbuilt functions, but I get the impression the exercises want me to do them manually...

def one(i1, i2, i3):
    max_value = i1

    for value in i2, i3:
        if value > max_value:
            max_value = value

    return max_value


def two(value_list):
    total = 0

    for value in value_list:
        total += value

    return total


def three(values):
    total = 1

    for value in values:
        total *= value

    return total


def four(value):
    return value[::-1]


def five(value):
    if value < 1:
        return 0

    return value * five(value-1)


def six(value, lower, higher=math.inf):
    return lower <= value <= higher


def seven(value):
    s1 = f"No. of upper case characters: {sum(char.isupper() for char in value)}"
    s2 = f"No. of lower case characters: {sum(char.islower() for char in value)}"

    return s1, s2


def eight(value):
    return sorted(set(value))


def nine(value):
    if value < 2:
        return False

    limit = int(math.sqrt(value))
    return all(value % n for n in range(2, limit + 1))


print(nine(2))