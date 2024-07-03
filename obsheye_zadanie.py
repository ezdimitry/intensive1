class A:
    '''Класс A
    Устанавливает значение атрибута a
    Возвращает значение атрибута a'''
    def set_a(self, value):
        self.a = value
    def get_a(self):
        '''.'''
        return self.a


class B:
    '''Класс B
    Инициализирует экземпляр класса B с атрибутом b
    Возвращает значение атрибута b'''

    def __init__(self, b):
        self.b = b
    def get_b(self):
        return self.b


class C(A, B):
    '''Класс C = A + B
    Инициализирует экземпляр класса C с атрибутами a, b, c
    Устанавливает значение атрибута b
    Устанавливает значение атрибута c
    Возвращаем значение атрибута c'''

    def __init__(self, a, b, c):
        A.__init__(self)
        B.__init__(self, b)
        self.a = a
        self.c = c

    def set_b(self, value):
        self.b = value
    def set_c(self, value):
        self.c = value
    def get_c(self):
        return self.c


class D:
    '''Класс D содержит методы для вывода словарей атрибутов
    Выводит на экран словарь атрибутов переданного объекта
    Выводит на экран словарь атрибутов своего класса'''

    @staticmethod
    def stat_print_dict(obj):
        print(obj.__dict__)
    @classmethod
    def cls_print_dict(cls):
        '''.'''
        print(cls.__dict__)

a = A()
a.set_a(10)
print(a.get_a())

b = B(20)
print(b.get_b())

c = C(10, 20, 30)
print(c.get_a())
print(c.get_b())
print(c.get_c())

D.stat_print_dict(c)
D.cls_print_dict()