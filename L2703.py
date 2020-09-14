class Person():
    age = 3
    def __init__(self, name):
        self.name = name

print(Person.__name__)
print(Person.__class__)
print(list(Person.__dict__.items()))