def duplicates_remove(list1):
    sample_set = set(list1)
    print(list(sample_set))


if __name__ == '__main__':
    list1 = [2, 4, 4, 7, 1, 3, 2, 5, 6, 7]
    duplicates_remove(list1)