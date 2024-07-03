"""Медведев Дмитрий Алексеевич, 1 вариант
Найдите три ключа с самыми высокими значениями в словаре my_dict
код задачи 5"""


my_dict = {'a': 5, 'b': 9, 'c': 2, 'd': 12, 'e': 7}
high_znac = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
print(high_znac)