def series(num):
    i = 0
    n1 = 0
    n2 = 1
    if num < 0:
        print("Enter Positive Number")
    elif num == 1:
        print(n1)
    elif num > 1:
        while i < num:
            print(n1, end=" ")
            sum = n1 + n2
            n1 = n2
            n2 = sum
            i += 1


if __name__ == '__main__':
    num = int(input("Enter the Range : "))
    series(num)
