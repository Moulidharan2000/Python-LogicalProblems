nums_list = [i for i in range(1, 10)]
print(nums_list)

even_list = [i for i in nums_list if i % 2 == 0]
print(even_list)

odd_list = [j for j in nums_list if j % 2 != 0]
print(odd_list)

square_list = [i**2 for i in nums_list]
print(square_list)

even_square_list = [i**2 for i in nums_list if i % 2 == 0]
print(even_square_list)

odd_square_list = [j**2 for j in nums_list if j % 2 != 0]
print(odd_square_list)

cube_list = [i**3 for i in nums_list]
print(cube_list)

new_list1 = [n**2 if n % 2 == 0 else n / 2 for n in nums_list]
print(new_list1)

new_list2 = [n**3 if n > 5 else n**2 if n % 2 == 0 else n / 2 for n in nums_list]
print(new_list2)

matrix = [[j for j in range(5)] for i in range(5)]
print(matrix)