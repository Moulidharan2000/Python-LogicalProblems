def reverse_int(num):
    rev = 0
    while num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        num //= 10
    print(rev)


if __name__ == '__main__':
    reverse_int(123)
    reverse_int(-4576)
