nums_list = [i for i in range(1, 11)]

even_set = {i for i in nums_list if i % 2 == 0}
print(even_set)

odd_set = {j for j in nums_list if j % 2 != 0}
print(odd_set)

new_set = {n ** 3 if n > 5 else n ** 2 if n % 2 == 0 else n / 2 for n in nums_list}
print(new_set)
