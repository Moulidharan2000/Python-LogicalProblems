def reverse(num):
    rev = 0
    while num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        num //= 10
    print("Reversed : ", rev)


if __name__ == "__main__":
    num = int(input("Enter the Number : "))
    reverse(num)
