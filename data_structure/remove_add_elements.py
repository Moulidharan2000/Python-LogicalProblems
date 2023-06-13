def position(list1):
    temp = 0
    for i in range(len(list1)):
        if i == 4:
            temp = list1.pop(i)
    print("After Removing the 4th index element : ", list1)
    for i in range(len(list1)):
        if i == 2:
            list1.insert(i, temp)
    print("After Adding element into 2nd index : ", list1)
    list1.append(temp)
    print("After Adding element in last : ", list1)


if __name__ == '__main__':
    list1 = [54, 44, 27, 79, 91, 41]
    print("Original List : ", list1)
    position(list1)
