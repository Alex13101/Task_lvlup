
'''Написать программу, которая принимает на вход список чисел и возвращает список,
содержащий только нечетные числа, умноженные на два. При этом, использовать
функции filter, map и лямбда-функцию.'''


def get_odd_doubled_numbers(lst):

    lst = [x * 2 for x in filter(lambda x: x & 1, lst)] #Побитовое сравнение х и 1 и если равны , то объект четный
                                                        # А конкретнее, то самый младший разряд в 2-й системе говорит
                                                        # о четности или нечетности числа
    return lst

# l = [10, 20, 30]
print(get_odd_doubled_numbers([1, 2, 3, 4, 5]))
print(get_odd_doubled_numbers([10, 20, 30]))
print(get_odd_doubled_numbers([]))
print(get_odd_doubled_numbers([1, 3, 5]))
print(get_odd_doubled_numbers([2, 4, 6]))
# odd_doubled_numbers(l)
# print(l)  # [2, 1]


#def get_odd_doubled_numbers(numbers: list) -> list:
    #pass

def test_get_odd_doubled_numbers():
    assert get_odd_doubled_numbers([1, 2, 3, 4, 5]) == [2, 6, 10]
    assert get_odd_doubled_numbers([10, 20, 30]) == []
    assert get_odd_doubled_numbers([]) == []
    assert get_odd_doubled_numbers([1, 3, 5]) == [2, 6, 10]
    assert get_odd_doubled_numbers([2, 4, 6]) == []
    print("All test_get_odd_doubled_numbers passed!")

test_get_odd_doubled_numbers()