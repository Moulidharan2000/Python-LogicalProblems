nums_list = [i for i in range(1, 11)]

even_dict = {i: i ** 2 for i in nums_list if i % 2 == 0}
print(even_dict)

odd_dict = {j: j ** 3 for j in nums_list if j % 2 != 0}
print(odd_dict)

state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']

output_dict = {key: value for (key, value) in zip(state, capital)}
print(output_dict)

new_dict = {i: i ** 3 if i > 5 else i ** 2 if i % 2 == 0 else i / 2 for i in nums_list}
print(new_dict)
