# -----------------------------------------------------------------------------
# Name:        Sorting
#
# Purpose:     Interactive sorting gui in python
#
# Author:      Daniel Di Giovanni
#
# Created:     03/26/2020
# -----------------------------------------------------------------------------

from tkinter import *
from random import *
import time
import copy
from config import *
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort_initialize


class Item:

    def __init__(self, top, j, canvas, colour):
        self.value = randint(1, top)
        self.colour = (0, 0, 255)
        self.iteration = j

        self.object = canvas.create_rectangle(
            space + wi * self.iteration, le - self.value,
            space + wi * (self.iteration + 1),
            le, fill=colour)

    def draw(self, canvas, colour):
        canvas.create_rectangle(
            space + wi * self.iteration, le - user_list[self.iteration].value,
            space + wi * (self.iteration + 1),
            le, fill=colour)


def generate_random_list(top, canvas):

    random_list = [None] * 64
    global user_list

    for i in range(64):
        random_list[i] = Item(top, i, canvas, "blue")

    user_list = random_list


def draw_list(canvas, size):
    """Draws list, no animations"""

    canvas.delete("all")

    # Change user list (global) with this function call
    generate_random_list(int(size[1]*0.8), canvas)


def change_sleep(value):
    global stopper
    stopper = value / 1000000


def main():

    root = Tk()

    root.title("Sorting Visualization")

    global user_list
    size = (1100, 700)

    # Create and place canvases (one for banner, one for list rectangles)
    back = Canvas(root, width=1100, height=500)
    banner = Frame(root, bg="black")

    button_frame = Frame(banner, bg="black")

    # Create and place buttons
    b_rand = Button(
        button_frame, text="Generate Random List", padx=10, pady=10,
        command=lambda: draw_list(back, size))
    # b_list = Button(button_frame, text="Create a List", padx=10, pady=10)
    b_bub = Button(
        button_frame, text="Bubble Sort", padx=10, pady=10,
        command=lambda: bubble_sort(root, back, user_list))
    b_select = Button(
        button_frame, text="Selection Sort", padx=10, pady=10,
        command=lambda: selection_sort(root, back, user_list))
    b_insert = Button(
        button_frame, text="Insertion Sort", padx=10, pady=10,
        command=lambda: insertion_sort(root, back, user_list))
    b_merge = Button(
        button_frame, text="Merge Sort", padx=10, pady=10,
        command=lambda: merge_sort_initialize(root, back, user_list))

    back.pack(fill=BOTH)
    banner.pack(fill=BOTH)

    button_frame.pack(anchor=CENTER)

    b_rand.pack(side=LEFT, padx=10, pady=10)
    # b_list.pack(side=LEFT, padx=10, pady=10)
    b_bub.pack(side=LEFT, padx=10, pady=10)
    b_select.pack(side=LEFT, padx=10, pady=10)
    b_insert.pack(side=LEFT, padx=10, pady=10)
    b_merge.pack(side=LEFT, padx=10, pady=10)

    slider = Scale(root, from_=0, to=100, orient=HORIZONTAL)
    slider.place(x=int(size[0]*0.8), y=int(size[1]*0.87))
    slider_button = Button(
        root, text="Set Value", command=lambda: change_sleep(slider.get()))
    slider_button.place(x=int(size[0]*0.8), y=int(size[1]*0.9)+20)

    root.mainloop()


if __name__ == "__main__":
    main()
