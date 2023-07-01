# Single level inheritance and multi level inheritance
class Animal:
    def run(self):
        print("Animal is running")


class Dog(Animal):
    def run(self):
        print("Dog is running")

    def sound(self):
        print("Dog is Barking")


class Cat(Dog):
    def run(self):
        print("Cat is running")

    def sound(self):
        print("Cat is meowing")


if __name__ == '__main__':
    animal = Animal()
    animal.run()

    dog = Dog()
    dog.run()
    dog.sound()

    cat = Cat()
    cat.run()
    cat.sound()


# multiple inheritance--------------------------------
class Calculation1:
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b


class Calculation2:
    def multiply(self, a, b):
        return a * b


class Derived(Calculation1, Calculation2):
    def divide(self, a, b):
        return a / b


if __name__ == '__main__':
    derived = Derived()
    print(derived.sum(10, 40))
    print(derived.sub(30, 20))
    print(derived.multiply(20, 50))
    print(derived.divide(100, 5))

    print("issubclass : ", issubclass(Derived, Calculation1))
    print("issubclass : ", issubclass(Derived, Calculation2))
    print("issubclass : ", issubclass(Calculation1, Calculation2))
    print("issubclass : ", issubclass(Calculation2, Calculation1))

    print("isinstance : ", isinstance(derived, Derived))