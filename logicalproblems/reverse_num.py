def reverse(n):
    rev = 0
    while n != 0:
        rem = n % 10
        rev = rev * 10 + rem
        n //= 10
    return rev


if __name__ == '__main__':
    n = int(input("Enter the Number : "))
    print(reverse(n))
