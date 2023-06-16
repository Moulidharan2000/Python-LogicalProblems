def pair(first_list, second_list):
    third = zip(first_list, second_list)
    print(tuple(third))


if __name__ == '__main__':
    first_list = [2, 3, 4, 5, 6, 7, 8]
    second_list = [4, 9, 16, 25, 36, 49, 64]
    pair(first_list, second_list)