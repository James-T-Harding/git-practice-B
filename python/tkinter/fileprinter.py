from tkinter import Tk, Label, filedialog, Button


def open_file(event):
    path = filedialog.askopenfilename()

    with open(path) as f:
        for no, line in enumerate(f.readlines()):
            label = Label(root, text=line.strip('\n'))
            label.grid(column=1, row=no+1)


root = Tk()
open_button = Button(root, text="Open")
open_button.grid(column=0, row=0)
open_button.bind("<ButtonRelease-1>", open_file)


if __name__ == "__main__":
    root.mainloop()
