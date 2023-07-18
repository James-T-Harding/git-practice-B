import random


def e1():
    print(*(str(r) for r in range(1500, 2701) if not r % 5 or not r % 7))


def e2():
    temperature = input("Temperature Here: ")
    
    match int(temperature[:-1]), temperature[-1]:
        case fahrenheit, "F" | "f":
            celsius = 5 * (fahrenheit - 32) / 9
            print(f"{fahrenheit} F is {round(celsius)} C")
        case celsius, "C" | "c":
            fahrenheit = 32 + 9 * celsius / 5
            print(f"{celsius} C is {round(fahrenheit)} F")


def e3():
    print("Guess a number between one and ten until you get it right: ")
    answer = random.randint(1, 9)

    while int(input(">")) != answer:
        pass

    print("Well guessed!")


def e4():
    no = 1
    inc = 1

    while no > 0:
        print(" ".join(no * ['*']))

        if no == 5:
            inc = -1

        no += inc


def e5():
    word = input("Input word: ")
    print(word[::-1])


def e6():
    sample_numbers = (1, 2, 4, 4, 5, 6, 7, 8, 12)

    odd = sum(n % 2 for n in sample_numbers)
    even = len(sample_numbers) - odd

    print(f"Number of even numbers: {even}")
    print(f"Number of odd numbers: {odd}")


def e7():
    data_list = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section":'A'}]

    for item in data_list:
        print(f"Type of {item} is {type(item)}")


def e8():
    for n in range(7):
        if n in (3, 6):
            continue

        print(n)

