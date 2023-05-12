
'''Создание класса "Калькулятор" с методами для выполнения математических операций
 (сложение, вычитание, умножение, деление).
 Реализовать также возможность сохранения результатов операций в памяти калькулятора и их отображения.'''


class Calculator:
    def __init__(self):
        self.result = None
        self.memory = []

    def add(self, x, y):
        self.result = x + y

    def subtract(self, x, y):
        self.result = x - y

    def multiply(self, x, y):
        self.result = x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Деление на ноль невозможно")
        self.result = x / y

    def memorize_result(self):
        self.memory.append(self.result)

    def show_results(self):
        print(f"Результат операции: {self.result}")

    def show_memory(self):
        print("История операций:")
        for i, value in enumerate(self.memory, 1):
            print(f"{i}: {value}")



calc = Calculator()

calc.add(5, 3)
calc.memorize_result()

calc.subtract(5, 3)
calc.memorize_result()

calc.multiply(5, 3)
calc.memorize_result()

calc.divide(5, 3)
calc.memorize_result()

calc.show_results()

calc.show_memory()
