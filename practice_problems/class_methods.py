class Sample:
    number1 = 40
    number2 = 10

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print(self.number1)
        return self.num1 + self.num2

    @classmethod
    def sub(cls):
        return cls.number1 - cls.number2

    @staticmethod
    def multi(a, b):
        return a * b


add = Sample(10, 40)
print(add.add())
print(Sample.sub())
print(Sample.multi(2, 50))
