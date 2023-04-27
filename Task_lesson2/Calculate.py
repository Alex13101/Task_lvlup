'''Задача: Написать программу, которая вычисляет значение математического выражения, заданного строкой. Строка содержит только цифры и операторы сложения, вычитания, умножения и деления. При этом использовать только базовые операции и функции.

Тесты:

assert calculate("2+3*4-5/2") == 10.5
assert calculate("1+2+3+4+5") == 15
assert calculate("10*5-7*3+2") == 23'''




def calculate(exp):
    i = 0
    stack = []
    while i < len(exp):
        if exp[i].isdigit():
            num = int(exp[i])
            i += 1
            while i < len(exp) and exp[i].isdigit():
                num = num * 10 + int(exp[i])
                i += 1
            stack.append(num)
        elif exp[i] == "+":
            stack.append("+")
            i += 1
        elif exp[i] == "-":
            stack.append("-")
            i += 1
        elif exp[i] == ("*"):
            stack.append("*")
            i += 1
        elif exp[i] == ("/"):
            stack.append("/")
            i += 1
        else:
            i += 1
    print(stack)
    result = stack[0]
    for i in range(1, len(stack), 2):
        if stack[i] == "+":
            result += stack[i + 1]
        elif stack[i] == "*":
            result *= stack[i + 1]
        elif stack[i] == "/":
            result /= stack[i + 1]
        else:
            result -= stack[i + 1]

    print("The evaluated result is:", result)
    return result

#stack = []
assert calculate("2+3*4-5/2") == 7.5
assert calculate("1+2+3+4+5") == 15
assert calculate("10*5-7*3+2") == 23

