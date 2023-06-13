def palindrome(num):
    rev = 0
    temp = num
    while num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        num //= 10
    if temp == rev:
        print(temp, "is Palindrome")
    else:
        print(temp, "is not a Palindrome")


if __name__ == '__main__':
    num = int(input("Enter the Number : "))
    palindrome(num)
