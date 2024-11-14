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
def converter_list(a):
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
root.geometry("600x400+250+100")
root.resizable(False, False)

#LABELS
first_row = tk.Label(text = "Coordinates of boxes:", font = ("Arial", 14))
row_with_coordinates = tk.Label(text = converter_list(coordinates_of_boxes), font = ("Arial", 14))
how_enter = tk.Label(text = "Enter coordinates without commas:", font = ("Arial", 14))
correct_answer = tk.Label(text = "We found boxes!", font = ("Arial", 14))
incorrect_answer = tk.Label(text = "Oh no boxes moved!", font = ("Arial", 14), foreground = "red")

#FUNCTIONS FOR BUTTONS
def checker():
    global coordinates_of_boxes

    is_digit = False
    mean = place_for_numbers.get()
    mean = mean.split()
    sumer = 0
    for i in mean:
        if i.isdigit():
            sumer += 1
    if sumer == len(mean):
        is_digit = True

    if is_digit:
        for i in range(len(mean)):
            mean[i] = int(mean[i])

        if set(mean) == set(coordinates_of_boxes):
            first_row.grid_forget()
            row_with_coordinates.grid_forget()
            how_enter.grid_forget()
            place_for_numbers.grid_forget()
            button_check.grid_forget()

            correct_answer.grid(row = 0, column = 0)
            button_complete.grid(row = 1, column = 1, stick = "e")
        else:
            place_for_numbers.delete(0, tk.END)
            incorrect_answer.grid(row=3, column=0)
            generator_of_means(coordinates_of_boxes)
            row_with_coordinates["text"] = converter_list(coordinates_of_boxes)
    else:
        place_for_numbers.delete(0, tk.END)
        incorrect_answer.grid(row = 3, column = 0)
        generator_of_means(coordinates_of_boxes)
        row_with_coordinates["text"] = converter_list(coordinates_of_boxes)

def completer():
    root.destroy()

#BUTTONS
button_check = tk.Button(text = "check", command = checker, font = ("Arial", 14))
button_complete = tk.Button(text = "complete", command = completer, font = ("Arial", 14))

#ENTRIES
place_for_numbers = tk.Entry(font = ("Arial", 14))

#PLACEMENT OF OBJECTS
first_row.grid(row = 0, column = 0)
row_with_coordinates.grid(row = 0, column = 1)
how_enter.grid(row = 1, column = 0)
place_for_numbers.grid(row = 1, column = 1)
button_check.grid(row = 2, column = 1, stick = "e")

root.mainloop()