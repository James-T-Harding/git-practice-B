authors = {
    "Casey Simmons": ["The wonderful world of os", "Return to the wonderful world of os"],
    "Jarathteh Nolans": ["End times", "Final Times", "The End", "Last Stand"],
    "Endas Newperson": ["My first book (please dont be mean)"]
}

if __name__ == "__main__":
    author_name = input("Author name: ")

    if books := authors.get(author_name):
        print(", ".join(sorted(books)))