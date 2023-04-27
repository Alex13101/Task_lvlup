'''Задача: Написать программу, которая принимает на вход число и выводит на экран все простые числа до этого числа. При этом использовать только базовые операции, цикл for, функции и оператор присваивания.

Тесты:'''



def prime_numbers(n):
    num =[]
    for number in range(0, n + 1):
        if number > 1:
            for i in range(2, number):
                if(number % i) == 0:
                    break
            else:
                num.append(number)
    return num
print(prime_numbers(10))
print(prime_numbers(20))
print(prime_numbers(5))
assert prime_numbers(10) == [2, 3, 5, 7]
assert prime_numbers(20) == [2, 3, 5, 7, 11, 13, 17, 19]
assert prime_numbers(5) == [2, 3, 5]
