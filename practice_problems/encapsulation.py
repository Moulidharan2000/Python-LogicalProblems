# public members
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def old(self):
        print("Age : ", self.age)


if __name__ == '__main__':
    person = Person("Raj", 25)
    print("Name : ", person.name)
    person.old()


# private members
class Rectangle:
    __length = 0
    __breadth = 0

    def __init__(self):
        self.__length = 5
        self.__breadth = 3

    def area(self):
        print("\nArea : ", self.__length * self.__breadth)


if __name__ == '__main__':
    rect = Rectangle()
    rect.area()


# protected members
class Details:
    _name = "Jason"
    _age = 35
    _job = "Developer"


class Employee(Details):
    def details(self):
        print("\nName : ", self._name)
        print("Age : ", self._age)
        print("Job : ", self._job)


if __name__ == '__main__':
    emp_obj = Employee()
    emp_obj.details()
