num = int(input("Enter the num : "))
temp = 1
for i in range(num):
    i = i+1
    fact = temp * i
    temp = fact
print("The Factorial of ",num," is ",fact)