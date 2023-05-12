

class Phonebook:
    contacts = []

    def __init__(self, name,  phone):
        self.name = name
        self.phone = phone

        self.__class__.contacts.append(self)

    def change_phone(self, new_phone):
        self.phone = new_phone

    @classmethod
    def add_contact(cls, contact):  #
        cls.contacts.append(contact)

    @classmethod
    def remove_student(cls, name):

        for contact in cls.contacts:
            if contact.name == name:
                print(f"Удаляем {contact.name}, c номером {contact.phone}")
                cls.contacts.remove(contact)
        else:
            print(f"Поиск контакта {name} завершен")

    @classmethod
    def print_contacts(cls):
        for contact in cls.contacts:
            print(f"{contact.name} {contact.phone} \n")

    @classmethod
    def search_contacts(cls, name):
        is_stud = False
        for contact in cls.contacts:
            if contact.name == name:
                print(f"Найден {contact.name} с номером {contact.phone}")
                is_stud = True

        if not is_stud:
            print(f"Контакт  {name} не найден")




contact1 = Phonebook("Иван Иванов", "+7 (111) 111-11-11")
contact2 = Phonebook("Петр Петров", "+7 (222) 222-22-22")

# добавляем контакт
contact3 = Phonebook("Сергей Сергеев", "+7 (333) 333-33-33")
Phonebook.add_contact(contact3)

# изменяем данные контакта
contact1.change_phone("+7 (444) 444-44-44")

# выводим информацию о всех контактах
Phonebook.print_contacts()

# ищем контакт по имени
Phonebook.search_contacts("Петр Петров")