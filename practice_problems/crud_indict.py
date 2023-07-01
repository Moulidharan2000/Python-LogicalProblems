sample_dict = {1: 2, 2: 4}
print(sample_dict)

sample_dict.update({3: 5})
print(sample_dict)

sample_dict.pop(2)
print(sample_dict)

print(sample_dict.get(3))

sample_list = [2, 1, 3]
print(sample_list)

sample_list.append(5)
print(sample_list)

sample_list.pop(1)
print(sample_list)

print(sample_list)

for i in range(len(sample_list)):
    if sample_list[i] == 5:
        sample_list[i] = 4
print(sample_list)

sample_list[2] = 6
print(sample_list)

sample_list.insert(2, 7)
print(sample_list)
