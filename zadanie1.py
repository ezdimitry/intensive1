"""Медведев Дмитрий Алексеевич, 1 вариант
Декоратор считающий количество вызовов функции
код задачи 1"""


def decorator(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"функция {func.__name__} вызвалась {wrapper.calls} раз")
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper

@decorator
def func():
    print('функция выполнилась')


func()
func()
func()