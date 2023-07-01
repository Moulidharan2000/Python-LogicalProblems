# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#
#     @abstractmethod
#     def run(self):
#         pass
#
#
# class Dog(Animal):
#     def run(self):
#         print("Dog is running...")
#
#     def sleep(self):
#         print("Dog sleeping...")
#
#
# if __name__ == '__main__':
#     dog = Dog()
#     dog.run()
#     dog.sleep()
#
#
# class Calculation:
#
#     def add(self, a, b):
#         c = a + b
#         print(c)
#
#     def add(self, a, b, c):
#         d = a + b + c
#         print(d)
#
#
# if __name__ == '__main__':
#     calc = Calculation()
#     calc.add(4, 7, 5)
#     calc.add(2, 6, 8)
#
#
# class Vehicle1:
#
#     def run(self):
#         print("Vehicle is running")
#
# class Vehicle2:
#
#     def stop(self):
#         pass
#
# class Tata(Vehicle1):
#
#     def run(self):
#         print("Tata Car is running")
#
#
# class Honda(Vehicle1):
#
#     def run(self):
#         print("Honda Car is running")
#
#
# if __name__ == '__main__':
#     vehicle = Vehicle1()
#     vehicle.run()
#
#     tata = Tata()


# num_dict = {i: i ** 2 for i in range(10) if i % 2 == 0}
# print(num_dict)

# Run–length encoding (RLE) is a simple form of lossless data compression that runs on sequences with the same value occurring many consecutive times. It encodes the sequence to store only a single value and its count.
#
# Input: 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
# Output: '12W1B12W3B24W1B14W'
# Explanation: String can be interpreted as a sequence of twelve W’s, one B, twelve W’s, three B’s, and so on..

def encode(sample):
    encoding = ""
    i = 0
    while i < len(sample):
        count = 1
        while i+1 < len(sample) and sample[i] == sample[i + 1]:
            count += 1
            i += 1
        encoding += str(count)+sample[i]
        i += 1
    print(encoding)


if __name__ == '__main__':
    sample = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
    encode(sample)
