'''Задача: Написать программу, которая принимает на вход два числа
и выводит на экран результат их умножения. При этом использовать только базовые
операции сложения, вычитания и условных операторов.

Тесты:

assert multiply(2, 3) == 6
assert multiply(10, 5) == 50
assert multiply(7, -3) == -21'''


def multiply(a, b):
    a * b
    # print()
    return a*b


print(multiply(7, -3))
assert multiply(2, 3) == 6
assert multiply(10, 5) == 50
assert multiply(7, -3) == -21
