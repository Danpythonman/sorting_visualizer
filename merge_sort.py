import time
import copy
from config import *


def merge_sort_initialize(master, canvas, user_list):

    merge_sort(user_list, 0, len(user_list), master, canvas)


def merge_sort(arr, left, right, master, canvas):

    mid = (left + right) // 2
    if left + 1 < right:
        merge_sort(arr, left, mid, master, canvas)
        merge_sort(arr, mid, right, master, canvas)
        merge(arr, left, mid, right, master, canvas)


def merge(arr, start, middle, end, master, canvas):

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
