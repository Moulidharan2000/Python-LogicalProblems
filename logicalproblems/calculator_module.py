# addition function
def add(a, b):
    return a + b


# subtraction function
def sub(a, b):
    return a - b


# multiplication function
def multiply(a, b):
    return a * b


# division function
def divide(a, b):
    return a / b


if __name__ == '__main__':
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    option = int(input("Enter the Options : "))
    if 0 <= option <= 4:
        a = int(input("Enter the Number 1 : "))
        b = int(input("Enter the Number 2 : "))
        if option == 1:
            print(add(a, b))
        elif option == 2:
            print(sub(a, b))
        elif option == 3:
            print(multiply(a, b))
        elif option == 4:
            print(divide(a, b))
    else:
        print("Invalid Option")
