from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass


class Tata(Car):
    def mileage(self):
        print("The mileage is 50 kmph")


class Honda(Car):
    def mileage(self):
        print("The mileage is 30 kmph")


if __name__ == '__main__':
    tata = Tata()
    tata.mileage()

    honda = Honda()
    honda.mileage()
