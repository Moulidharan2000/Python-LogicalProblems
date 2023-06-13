num = int(input("Enter the Number : "))
i = 1
temp = 1
while i<=num:
    fact = i*temp
    temp = fact
    i += 1
print("Factorial of",num,"is",fact)
