def count(num_list):
    occur_dict = {}
    for i in num_list:
        if i in occur_dict:
            occur_dict[i] += 1
        else:
            occur_dict[i] = 1
    print(occur_dict)


if __name__ == '__main__':
    num_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
    count(num_list)