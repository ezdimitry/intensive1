"""Медведев Дмитрий Алексеевич, 1 вариант
Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
код задачи 9"""

def change(lst):
    if len(lst) < 2:
        return lst
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

my_list = [1, 2, 3, 4, 5]
changed_list = change(my_list)
print(changed_list)