import Date.py

class Persona:
    __name = str
    __birthday = Date
    __age = int

    def Persona(name, birthday):
        self.__name = name
        self.__birthday = birthday
        self.__age = 2024 - int(birthday.year)
