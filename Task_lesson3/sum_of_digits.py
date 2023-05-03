'''Напишем рекурсивную функцию, которая вычисляет сумму цифр числа.'''


from sort_numbers import timer # импортируем декоратор времени выполнения



def sum_of_digits(digits):
    if digits < 10:
        return digits
    else:
        dig = digits % 10 # Остаток от деления аргумента на 10, т.е. крайняя цифра в числе

        result = dig + sum_of_digits(digits // 10) # (digits//10) результат целочисленного деления

        return result




print(sum_of_digits(12345))

@timer # оспользуем декоратор времени выполнения
def test_sum_of_digits():

    assert sum_of_digits(0) == 0
    assert sum_of_digits(5) == 5
    assert sum_of_digits(10) == 1
    assert sum_of_digits(12345) == 15
    assert sum_of_digits(999999999999999) == 135
    print("All test_sum_of_digits pass")


test_sum_of_digits()
