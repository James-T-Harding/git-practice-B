def take_grades(name, homework, assessment, final):
    average = (4 * homework + 2 * assessment + final) / 3
    grade_boundaries = [('A', 80), ('B', 70), ('C', 60), ('D', 50), ('F', 40)]

    grade = 'A*'

    for symbol, value in grade_boundaries:
        if average < value:
            grade = symbol

    return f"{name}: {average:.2f}% - {grade}"


name = input("Name: ")
scores = [input(f"{prompt} Score: ") for prompt in ("Homework", "Assessment", "Final")]
result = take_grades(name, *map(int, scores))

print(result)