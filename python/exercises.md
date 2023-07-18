### Tutorial - Variable types

#### Integers and Floats
[input1 as an int]
[input2 as a float]
[input2 2 rounded as an int]

#### Boolean
Makes several print statements, each separate input to pring joined with a space. The overall output is:

My pet is called Pep Guardogiola , He is 3 years old.
Statement: Pep Guardogiola barks. True
Statement: Pep Guardogiola tweets. False

### Collections - Exercise

```Python
authors = {
    "Casey Simmons": ["The wonderful world of os", "Return to the wonderful world of os"],
    "Jarathteh Nolans": ["End times", "Final Times", "The End", "Last Stand"],
    "Endas Newperson": ["My first book (please dont be mean)"]
}

author_name = input("Author name: ")

if books := authors.get(author_name):
    print(", ".join(sorted(books)))

```

### Decision-Making Exercise

```Python
mark = input("Mark: ")

if mark.isdigit():
    mark_value = int(mark)

    # With elif statement
    if mark_value > 85:
        print("Distinction")
    elif 65 < mark_value < 85:
        print("Pass")
    else:
        print("Fail")

    # Without elif statement
    print("Distinction" if mark_value > 85 else "Pass" if 65 < mark_value
```

### Loops
```Python
count = 0

while count < 5:
    print(input("Name: "), "is awesome.")
    count += 1
```