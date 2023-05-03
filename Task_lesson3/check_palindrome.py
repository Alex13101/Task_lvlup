'''Написать программу, которая считывает строку, проверяет,
является ли она палиндромом, и выводит сообщение о результате проверки.
При этом, использовать функции reverse и рекурсию.'''


def check_palindrome(l):
    k = ''
    for i in reversed(l):
        k += i
    #print(k)
    if l == k:
        return True
    else:
        return False


def chek_polindrome_2(l):
    if len(l) < 1:
        return True
    else:
        if l[0] == l[-1]:
            return chek_polindrome_2(l[1:-1]) # Условие полиндрома
                                                #hello (первые 2  и последние два символа проверяются, если совподают,
                                                #то полиндромм )
        else:
            return False


# print(*reversed("hello"))
print(chek_polindrome_2("a"))


# def check_palindrome(s: str) -> bool:
#     pass

def test_check_palindrome():
    assert check_palindrome("racecar") == True
    assert check_palindrome("hello") == False
    assert check_palindrome("level") == True
    assert check_palindrome("") == True
    assert check_palindrome("a") == True
    assert check_palindrome("ab") == False
    print("All test_check_palindrome passed!")





def test_check_palindrome_2():
    assert chek_polindrome_2("racecar") == True
    assert chek_polindrome_2("hello") == False
    assert chek_polindrome_2("level") == True
    assert chek_polindrome_2("") == True
    assert chek_polindrome_2("a") == True
    assert chek_polindrome_2("ab") == False
    print("All test_check_palindrome passed!")

test_check_palindrome()


test_check_palindrome_2()
