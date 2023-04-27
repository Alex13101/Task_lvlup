'''Задача: Написать программу, которая принимает на вход три числа и определяет, являются ли они пифагоровой тройкой. При этом использовать только базовые операции и условные операторы.

Тесты:

assert is_pythagorean_triple(3, 4, 5) == True
assert is_pythagorean_triple(5, 12, 13) == True
assert is_pythagorean_triple(7, 8, 9) == False'''

def is_pythagorean_triple(a,b,c):
    if (a**2)+(b**2) == c**2:
        return True
    else:
        return False


assert is_pythagorean_triple(3, 4, 5) == True
assert is_pythagorean_triple(5, 12, 13) == True
assert is_pythagorean_triple(7, 8, 9) == False

