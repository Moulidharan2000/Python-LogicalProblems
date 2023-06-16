def inbulit_functions(num_list):
    num_list.append(10)
    print("Appending element : ", num_list)

    num_list.copy()
    print("Copy of list : ", num_list)

    temp = num_list.count(6)
    print("Count element 6 : ", temp)

    num_list.extend([4, 7, 8])
    print("Extending element : ", num_list)

    temp = num_list.index(8)
    print("Element 8 at index : ", temp)

    num_list.insert(12, 5)
    print("Inserting element 5 at index 12 : ", num_list)

    num_list.pop(4)
    print("Pop element : ", num_list)

    num_list.remove(5)
    print("Remove element : ", num_list)

 #   num_list.remove('h')
 #   print("Reversing list : ", num_list)

    num_list.sort()
    print("Sorted list : ", num_list)

    num_list.clear()
    print("Clearing elements in list : ", num_list)


if __name__ == '__main__':
    num_list = [2, 3, 5, 4, 6, 7, 8, 1, 9, 6]
    inbulit_functions(num_list)
