def take_grades(name, homework, assessment, final):
    average = (homework + assessment + final) / 3

    return f"{name} : {average:.2f}"


prompts = []

name = input("Name: ")
scores = [input(f"{prompt} Score: ") for prompt in ("Homework", "Assessment", "Final")]

print(take_grades(name, *map(int, scores)))