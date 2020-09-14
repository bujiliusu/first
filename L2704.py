def add_name(name):
    def wrapper(cls):
        cls.NAME = name
        return cls
    return wrapper
@add_name('tom')
class Person: # Person = add_name(Person)
    AGE = 20
print(Person.__dict__)
