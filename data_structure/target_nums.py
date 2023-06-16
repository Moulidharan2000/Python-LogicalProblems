def add_nums(num_list, target):
    temp1 = 0
    temp2 = 0
    for i in range(len(num_list)):
        for j in range(len(num_list)):
            if num_list[i] + num_list[j] == target:
                temp1 = j
                temp2 = i
                break
    print(temp1, temp2)


if __name__ == '__main__':
    num_list = [2, 3, 7, 11, 15]
    target = int(input("Enter the Target Number : "))
    add_nums(num_list, target)
