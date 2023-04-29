'''Задача: Написать программу, которая вычисляет значение математического выражения, заданного строкой. Строка содержит только цифры и операторы сложения, вычитания, умножения и деления. При этом использовать только базовые операции и функции.

Тесты:

assert calculate("2+3*4-5/2") == 10.5
assert calculate("1+2+3+4+5") == 15
assert calculate("10*5-7*3+2") == 23'''


def calculate(exp):
    # Определяем приоритеты операций
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    # Создаем стек для хранения операндов и операций
    stack = []
    # Создаем список для хранения обратной польской записи
    rpn = []
    i = 0
    while i < len(exp):
        if exp[i].isdigit():
            # Если символ является цифрой, то читаем число
            num = int(exp[i])
            i += 1
            while i < len(exp) and exp[i].isdigit():
                num = num * 10 + int(exp[i])
                i += 1
            # Добавляем число в обратную польскую запись
            rpn.append(num)
        elif exp[i] in ["+", "-", "*", "/"]:
            # Если символ является операцией, то помещаем ее в стек
            while stack and stack[-1] != "(" and precedence[exp[i]] <= precedence.get(stack[-1], 0):
                rpn.append(stack.pop())
            stack.append(exp[i])
            i += 1
        elif exp[i] == "(":
            # Если символ является открывающей скобкой, то помещаем ее в стек
            stack.append("(")
            i += 1
        elif exp[i] == ")":
            # Если символ является закрывающей скобкой, то извлекаем операции из стека
            while stack and stack[-1] != "(":
                rpn.append(stack.pop())
            if stack and stack[-1] == "(":
                stack.pop()
            i += 1
        else:
            # Пропускаем пробелы и другие символы
            i += 1
    # Извлекаем оставшиеся операции из стека
    while stack:
        rpn.append(stack.pop())
    # Вычисляем результат, используя обратную польскую запись
    stack = []
    for token in rpn:
        if isinstance(token, int):
            # Если символ является числом, то помещаем его в стек
            stack.append(token)
        else:
            # Если символ является операцией, то извлекаем операнды из стека
            b = stack.pop()
            a = stack.pop()
            # Выполняем операцию и помещаем результат в стек
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(a / b)
    # Результат вычисления находится на вершине стека
    result = stack[-1]
    print("The evaluated result is:", result)
    return result

# def calculate(exp):
#     i = 0
#     stack = []
#     while i < len(exp):
#         if exp[i].isdigit():
#             num = int(exp[i])
#             i += 1
#             while i < len(exp) and exp[i].isdigit():
#                 num = num * 10 + int(exp[i])
#                 i += 1
#             stack.append(num)
#         elif exp[i] == "+":
#             stack.append("+")
#             i += 1
#         elif exp[i] == "-":
#             stack.append("-")
#             i += 1
#         elif exp[i] == ("*"):
#             stack.append("*")
#             i += 1
#         elif exp[i] == ("/"):
#             stack.append("/")
#             i += 1
#         else:
#             i += 1
#     print(stack)
#     result = stack[0]
#     for i in range(1, len(stack), 2):
#         if stack[i] == "+":
#             result += stack[i + 1]
#         elif stack[i] == "*":
#             result *= stack[i + 1]
#         elif stack[i] == "/":
#             result /= stack[i + 1]
#         else:
#             result -= stack[i + 1]

#     print("The evaluated result is:", result)
#     return result

#stack = []
# assert calculate("2+3*4-5/2") == 7.5
# assert calculate("1+2+3+4+5") == 15
# assert calculate("10*5-7*3+2") == 23

assert calculate("2+3*4-5/2") == 11.5
assert calculate("1+2+3+4+5") == 15
assert calculate("10*5-7*3+2") == 31
