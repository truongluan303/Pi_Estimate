import math
import random
from tkinter import *
from tkinter import Label

LIM = 1000  # constant


def createGUI():
    # Gui config
    root = Tk()
    root.geometry('500x170')
    root.title('Estimate Pi')

    # the actual GUI
    label1 = Label(root, text="Please enter the number of times the loop will run:")
    label1.pack()

    entry = Entry(root, width=30, bg="white", fg="dark blue", justify="center")
    entry.pack()

    space1 = Label(root)
    space1.pack()

    button = Button(root, text="RUN", bg="brown", fg="white",
                    command=lambda: simulate(int(entry.get())))
    button.pack()

    space2 = Label(root)
    space2.pack()

    global output_box
    output_box = Label(root, fg="brown")
    output_box.pack()

    root.mainloop()


def simulate(num_of_simulation):
    in_circle = 0

    for i in range(0, num_of_simulation):
        # generate a random coordinate for a point
        x = random.randint(0, LIM)
        y = random.randint(0, LIM)

        # check if the point is in the circle
        distance = float(math.sqrt((x * x) + (y * y)))
        if distance <= LIM:
            in_circle += 1

        if i % 100000 == 1:
            result = float(4 * in_circle / (i + 1))

    result = 4 * in_circle / num_of_simulation
    output_box.config(text="The final result is:\n" + str(result))
    print(result)


if __name__ == '__main__':
    createGUI()  # create the GUI
