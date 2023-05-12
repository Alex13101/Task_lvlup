

'''Создание класса "Студент" с атрибутами "имя", "фамилия",
"курс", "средний балл". Реализовать методы для добавления и удаления студента,
изменения данных студента, вывода информации о всех студентах,
а также поиска студента по фамилии.'''



class Student:
    students_list = []

    def __init__(self, first_name, last_name, course, average_score):
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
        self.average_score = average_score
        self.__class__.students_list.append(self)

    def change_course(self, new_course):
        self.course = new_course

    @classmethod
    def add_student(cls, student):  #
        cls.students_list.append(student)

    @classmethod
    def remove_student(cls, last_name):

        for student in cls.students_list:
            if student.last_name == last_name:
                print(f"Удаляем {student.first_name} {student.last_name}, {student.course} курс, средний балл {student.average_score}")
                cls.students_list.remove(student)
        else:
            print(f"Поиск студента {last_name} завершен")

    @classmethod
    def print_students(cls):
        for student in cls.students_list:
            print(f"{student.first_name} {student.last_name}, {student.course} курс, средний балл {student.average_score} \n")

    @classmethod
    def search_student(cls, last_name):
        is_stud = False
        for student in cls.students_list:
            if student.last_name == last_name:
                print(f"Найден {student.first_name} {student.last_name}, {student.course} курс, средний балл {student.average_score}")
                is_stud = True

        if not is_stud:
            print(f"Студент с фамилией {last_name} не найден")


Student("Иван", "Иванов", 3, 4.5)
Student("Петр", "Петров", 2, 3.7)

Student("Сергей", "Сергеев", 1, 4.0)
Student("Васечкин", "Вася", 4, 4.1)
Student("Игорь", "Жопов", 5, 3.2)
Student(input("Введите имя "), input("Введи фамилию "), input("Какой курс "), input("Средний бал "))

student3 = Student("Антоша", "Писин", 1, 4.0)
Student.add_student(student3) # При таком добавлении принтуется два раза ???
print(student3)
Student.print_students()

student3.change_course(4) # изменяем инфо студента
# Student.add_student(student4)
# Student.add_student(student5)

#Student.print_students()

#student1.change_course(4)
Student.remove_student(input("Кого удаляем?: "))

Student.print_students()

Student.search_student(input("Введите фамилию искомого студента: "))

Student.print_students()
