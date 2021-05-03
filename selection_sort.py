import time
from config import *


def find_min(start, user_list):
    """Finds the smallest item in a list starting at a given index"""

    minimum = start
    for j in range(start, len(user_list)):
        if user_list[minimum].value > user_list[j].value:
            minimum = j

    return minimum


def selection_sort(master, canvas, user_list):
    """Sorts the list using selection sort algorithm and draws rectangles
    representing items in the list as they are being sorted"""

    for i in range(len(user_list)):

        low = find_min(i, user_list)

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
