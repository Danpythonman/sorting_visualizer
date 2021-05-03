import time
from config import *


def bubble_sort(master, canvas, user_list):

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
