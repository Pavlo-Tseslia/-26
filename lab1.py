# Батьківський клас
class Humanity:
    def __init__(self, name, age):
        self.name = name          # публічний атрибут
        self.__age = age          # інкапсуляція (приватний атрибут)

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Вік має бути додатнім")

    def info(self):
        return f"Ім'я: {self.name}, Вік: {self.__age}"

    def role(self):
        return "Я — людина"


# Дочірній клас
class Student(Humanity):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    # Поліморфізм (перевизначення методу)
    def role(self):
        return "Я — студент"

    def info(self):
        return f"{super().info()}, Університет: {self.university}"


# Перевірка роботи
human = Humanity("Олексій", 35)
student = Student("Тарас", 18, "КНУ")

print(human.info())
print(human.role())

print(student.info())
print(student.role())
