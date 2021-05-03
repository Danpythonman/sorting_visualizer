import time
from config import *

def insertion_sort(master, canvas, user_list):

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
