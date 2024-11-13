import tkinter as tk
import random

#MAIN ELEMENTS

coordinates_of_boxes = []

#function for generate of means boxes
def generator_of_means(a):
    a.clear()
    helper = 0
    while len(a) != 3:
        helper = random.randint(1, 7)
        if helper not in a:
            a.append(helper)

#function which will convert list to row
def converter(a):
    row = ""
    for i in range(len(a)):
        if i != len(a) - 1:
            row += str(a[i]) + ", "
        else:
            row += str(a[i])
    return row

generator_of_means(coordinates_of_boxes)

#WINDOW
root = tk.Tk()

#CHARACTERISTICS OF WINDOW
root.title("Help for martians")
root.geometry("500x400+250+100")
root.resizable(False, False)

#LABELS
first_row = tk.Label(text = "Coordinates of boxes:", font = ("Arial", 14))
row_with_coordinates = tk.Label(text = converter(coordinates_of_boxes), font = ("Arial", 14))

#FUNCTIONS FOR BUTTONS

#BUTTONS

#ENTRIES
place_for_numbers = tk.Entry(font = ("Arial", 14))

#PLACEMENT OF OBJECTS
first_row.grid(row = 0, column = 0)
row_with_coordinates.grid(row = 0, column = 1)
place_for_numbers.grid(row = 2, column = 0)

root.mainloop()