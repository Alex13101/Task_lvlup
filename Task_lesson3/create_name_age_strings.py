
'''Допустим, у нас есть два списка одинаковой длины, names и ages,
содержащие соответственно имена и возрасты людей.
Мы хотим создать новый список строк, в которых будут указаны имена и возрасты в формате "Имя - возраст".
Напишите comprehension, который решает эту задачу'''



def create_name_age_strings(names, ages):
    new_string1 = []
    for i in range(len(names)):
        new_string = f"{names[i]} - {ages[i]}"
        new_string1.append(new_string)

    return new_string1

# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# print(create_name_age_strings(names, ages))




def test_create_name_age_strings():
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    expected = ['Alice - 25', 'Bob - 30', 'Charlie - 35']
    result = create_name_age_strings(names, ages)
    assert result == expected

    names = []
    ages = []
    expected = []
    result = create_name_age_strings(names, ages)
    assert result == expected
    print("All test_create_name_age_strings pass")

test_create_name_age_strings()