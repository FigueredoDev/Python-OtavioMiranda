

class NameMyMetaclass(type):
    def __new__(mcs, name, bases, namespace):
        print('new of metaclass')
        cls = super().__new__(mcs, name, bases, namespace)
        return cls


class Person(metaclass=NameMyMetaclass):
    def __new__(cls, *args, **kwargs):
        print("new of class")
        return super().__new__(cls)

    def __init__(self, name, lastname) -> None:
        print('Init of class')
        self.name = name
        self.lastname = lastname


"""def init_person(self, name, lastname):
    self.name = name
    self.lastname = lastname


Person = type("Person", (), {
    '__init__': init_person
})"""

print(type(Person))
person1 = Person("Jhonata", "Figueredo")
print(person1.name)
print(person1.lastname)
