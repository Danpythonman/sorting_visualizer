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


user_list = []
stopper = 0.1
mini_stopper = 0.025

s = (1100, 700)
space = int(s[0] * 0.08)
wi = (s[0] - 2 * space) // 64
le = int(s[1] * 0.8)


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


def bubble_sort(master, canvas):

    global user_list
    n = len(user_list)

    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):

            if user_list[i].value > user_list[i+1].value:

                canvas.delete(user_list[i].object)
                canvas.delete(user_list[i+1].object)

                user_list[i], user_list[i+1] = user_list[i+1], user_list[i]

                user_list[i].iteration = i
                user_list[i+1].iteration = i + 1

                user_list[i].object = canvas.create_rectangle(
                    space + wi * user_list[i].iteration,
                    le - user_list[i].value,
                    space + wi * (user_list[i].iteration + 1),
                    le, fill="blue")
                user_list[i+1].object = canvas.create_rectangle(
                    space + wi * user_list[i+1].iteration,
                    le - user_list[i+1].value,
                    space + wi * (user_list[i+1].iteration + 1),
                    le, fill="blue")

                time.sleep(stopper)

                swapped = True

            master.update()


def find_min(start):

    global user_list

    minimum = start
    for j in range(start, len(user_list)):
        if user_list[minimum].value > user_list[j].value:
            minimum = j

    return minimum


def selection_sort(master, canvas):

    global user_list

    for i in range(len(user_list)):

        low = find_min(i)

        canvas.delete(user_list[i].object)
        canvas.delete(user_list[low].object)

        user_list[i], user_list[low] = user_list[low], user_list[i]

        user_list[i].iteration = i
        user_list[low].iteration = low

        user_list[i].object = canvas.create_rectangle(
            space + wi * user_list[i].iteration,
            le - user_list[i].value,
            space + wi * (user_list[i].iteration + 1),
            le, fill="blue")
        user_list[low].object = canvas.create_rectangle(
            space + wi * user_list[low].iteration,
            le - user_list[low].value,
            space + wi * (user_list[low].iteration + 1),
            le, fill="blue")

        time.sleep(stopper)

        master.update()


def insertion_sort(master, canvas):

    global user_list

    for i in range(len(user_list)):
        current_item = user_list[i]
        j = i - 1
        while j >= 0 and current_item.value < user_list[j].value:
            user_list[j + 1] = user_list[j]
            user_list[j + 1].iteration = j + 1
            j -= 1
        user_list[j + 1] = current_item
        user_list[j + 1].iteration = j + 1

        time.sleep(stopper)

        # Drawing code
        canvas.delete("all")
        for k in range(len(user_list)):
            user_list[k].object = canvas.create_rectangle(
                space + wi * user_list[k].iteration,
                le - user_list[k].value,
                space + wi * (user_list[k].iteration + 1),
                le, fill="blue")
        master.update()


def merge_sort_2(master, canvas):

    global user_list

    merge_sort2(user_list, 0, len(user_list), master, canvas)


def merge_sort2(arr, left, right, master, canvas):

    mid = (left + right) // 2
    if left + 1 < right:
        merge_sort2(arr, left, mid, master, canvas)
        merge_sort2(arr, mid, right, master, canvas)
        merge2(arr, left, mid, right, master, canvas)


def merge2(arr, start, middle, end, master, canvas):

    left_size = middle - start
    right_size = end - middle
    left1 = [0] * left_size
    right1 = [0] * right_size

    for i in range(left_size):
        left1[i] = arr[start + i]
    for i in range(right_size):
        right1[i] = arr[middle + i]

    left = copy.deepcopy(left1)
    right = copy.deepcopy(right1)

    l = 0
    r = 0
    a = start
    i = start

    while l < left_size and r < right_size:
        if left[l].value < right[r].value:
            canvas.delete(arr[i].object)
            arr[a] = left[l]
            arr[a].iteration = a

            arr[a].object = canvas.create_rectangle(
                space + wi * arr[a].iteration,
                le - arr[a].value,
                space + wi * (arr[a].iteration + 1),
                le, fill="blue")
            master.update()

            l += 1
            a += 1
            i += 1

            time.sleep(mini_stopper)

        else:
            canvas.delete(arr[i].object)
            arr[a] = right[r]
            arr[a].iteration = a

            arr[a].object = canvas.create_rectangle(
                space + wi * arr[a].iteration,
                le - arr[a].value,
                space + wi * (arr[a].iteration + 1),
                le, fill="blue")
            master.update()

            r += 1
            a += 1
            i += 1

            time.sleep(mini_stopper)

    while l < left_size:
        canvas.delete(arr[i].object)
        arr[a] = left[l]
        arr[a].iteration = a

        arr[a].object = canvas.create_rectangle(
            space + wi * arr[a].iteration,
            le - arr[a].value,
            space + wi * (arr[a].iteration + 1),
            le, fill="blue")
        master.update()

        l += 1
        a += 1
        i += 1

        time.sleep(mini_stopper)

    while r < right_size:
        canvas.delete(arr[i].object)
        arr[a] = right[r]
        arr[a].iteration = a

        arr[a].object = canvas.create_rectangle(
            space + wi * arr[a].iteration,
            le - arr[a].value,
            space + wi * (arr[a].iteration + 1),
            le, fill="blue")
        master.update()

        time.sleep(mini_stopper)

        r += 1
        a += 1
        i += 1


def merge_sort(master, canvas, size):

    global user_list

    current_size = 1

    while current_size < len(user_list) - 1:
        # Left list indexes from (left) to (mid-1)
        # Right list indexes from (mid) to (right)
        left = 0
        right = 0
        mid = 0

        while left < len(user_list) - 1:

            time.sleep(stopper)

            # Left - start; Mid - middle; Right - end

            mid = left + current_size

            if mid > len(user_list) - 1:
                mid = len(user_list) - 1
                right = len(user_list)
            else:
                right = mid + current_size

            if right > len(user_list) - 1:
                right = len(user_list)

            merge(left, mid, right)

            # Drawing code
            canvas.delete("all")
            for k in range(len(user_list)):
                user_list[k].object = canvas.create_rectangle(
                    space + wi * user_list[k].iteration,
                    le - user_list[k].value,
                    space + wi * (user_list[k].iteration + 1),
                    le, fill="blue")
            master.update()

            left = right

        current_size *= 2


def merge(start, middle, end):

    global user_list

    # Initialize left and right lists
    left_size = middle - start
    right_size = end - middle
    left = [0] * left_size
    right = [0] * right_size

    for l in range(left_size):
        left[l] = user_list[l + start]
    for r in range(right_size):
        right[r] = user_list[middle + r]

    l = 0
    r = 0
    i = start

    while l < left_size and r < right_size:
        if left[l].value < right[r].value:
            user_list[i] = left[l]
            user_list[i].iteration = i
            l += 1
            i += 1
        else:
            user_list[i] = right[r]
            user_list[i].iteration = i
            r += 1
            i += 1

    while l < left_size:
        user_list[i] = left[l]
        user_list[i].iteration = i
        l += 1
        i += 1

    while r < right_size:
        user_list[i] = right[r]
        user_list[i].iteration = i
        r += 1
        i += 1


def change_sleep(value):
    global stopper
    stopper = value / 1000000


def main():

    root = Tk()

    global user_list
    size = (1100, 700)

    # Create and place canvases (one for banner, one for list rectangles)
    back = Canvas(root, width=1100, height=500)
    banner = Frame(root, bg="blue")

    button_frame = Frame(banner, bg="blue")

    # Create and place buttons
    b_rand = Button(
        button_frame, text="Generate Random List", padx=10, pady=10,
        command=lambda: draw_list(back, size))
    b_list = Button(button_frame, text="Create a List", padx=10, pady=10)
    b_bub = Button(
        button_frame, text="Bubble Sort", padx=10, pady=10,
        command=lambda: bubble_sort(root, back))
    b_select = Button(
        button_frame, text="Selection Sort", padx=10, pady=10,
        command=lambda: selection_sort(root, back))
    b_insert = Button(
        button_frame, text="Insertion Sort", padx=10, pady=10,
        command=lambda: insertion_sort(root, back))
    b_merge = Button(
        button_frame, text="Merge Sort", padx=10, pady=10,
        command=lambda: merge_sort_2(root, back))

    back.pack(fill=BOTH)
    banner.pack(fill=BOTH)

    button_frame.pack(anchor=CENTER)

    b_rand.pack(side=LEFT, padx=10, pady=10)
    b_list.pack(side=LEFT, padx=10, pady=10)
    b_bub.pack(side=LEFT, padx=10, pady=10)
    b_select.pack(side=LEFT, padx=10, pady=10)
    b_insert.pack(side=LEFT, padx=10, pady=10)
    b_merge.pack(side=LEFT, padx=10, pady=10)

    # slider = Scale(root, from_=0, to=100, orient=HORIZONTAL)
    # slider.place(x=int(size[0]*0.8), y=int(size[1]*0.87))
    # slider_button = Button(
    #     root, text="Set Value", command=lambda: change_sleep(slider.get()))
    # slider_button.place(x=int(size[0]*0.8), y=int(size[1]*0.9)+20)

    root.mainloop()


main()
