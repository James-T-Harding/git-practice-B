from functions import take_grades


class Student:
    def __init__(self, name, age, class_="student"):
        self.name = name
        self.age = age
        self.class_ = class_

    def print_grade(self, homework, assessment, final):
        print(take_grades(self.name, homework, assessment, final))


John = Student("John", "21")
Jane = Student("Jane", "22")

print(getattr(John, "name"))
John.print_grade(24, 45, 90)
