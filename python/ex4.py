
pass_values = set(range(66, 84))


if __name__ == "__main__":
    mark = input("Mark: ")

    if mark.isdigit():
        mark_value = int(mark)
        print("Distinction" if 85 < mark_value else "Pass" if 65 < mark_value < 85 else "Fail")