def isprime(num):
    flag = False
    if num == 1:
        print(num, "is not a Prime Number")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
        if flag:
            print(num, "is not a Prime Number")
        else:
            print(num, "is a Prime Number")


if __name__ == '__main__':
    num = int(input("Enter the Number : "))
    isprime(num)