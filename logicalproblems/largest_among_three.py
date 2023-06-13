def largest(num1, num2, num3):
    if num1 > num2 and num3:
        print(num1, "is Largest")
    elif num2 > num3 and num1:
        print(num2, "is Largest")
    elif num3 > num2 and num1:
        print(num3, "is Largest")


def smallest(num1, num2, num3):
    if num1 < num2 and num3:
        print(num1, "is Smallest")
    elif num2 < num3 and num1:
        print(num2, "is Smallest")
    elif num3 < num2 and num1:
        print(num3, "is Smallest")


if __name__ == '__main__':
    num1 = int(input("Enter the First Number : "))
    num2 = int(input("Enter the Second Number : "))
    num3 = int(input("Enter the Third Number : "))
    largest(num1, num2, num3)
    smallest(num1, num2, num3)