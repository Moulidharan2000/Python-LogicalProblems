def add(num):
    i = 1
    sum = 0
    while i <= num:
        sum += i
        i += 1
    return sum


if __name__ == '__main__':
    num = int(input("Enter the Number : "))
    print(add(num))
