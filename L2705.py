class Person:
    def __init__(self, name, age):
        self._name = name
        self.__age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        self.__age = value
tom = Person('tom', 18)
tom.age = 90
print(tom.age)
print(tom.__dict__)