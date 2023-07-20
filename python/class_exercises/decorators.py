def my_first_decorator(func):
    def wrapper(name):
        print("This is some new functionality!!")
        return func(name)

    return wrapper