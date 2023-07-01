def sum_odd_even(list1):
    temp_even = 0
    temp_odd = 0
    list2 = []
    even = 0
    odd = 0
    for i in list1:
        if i % 2 == 0:
            even = temp_even + i
            temp_even = even
        else:
            odd = temp_odd + i
            temp_odd = odd
    list2.append(even)
    list2.append(odd)
    print(list2)


if __name__ == '__main__':
    sum_odd_even([1, 2, 3, 4, 5, 6])
    sum_odd_even([3, 5, 4, 6, 7, 8])
