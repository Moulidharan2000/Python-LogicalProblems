def duplicates_remove(sample_list):
    sample_list2 = list()
    for i in sample_list:
        if i not in sample_list2:
            sample_list2.append(i)
    print("unique list :", sample_list2)
    sample_tuple = tuple(sample_list2)
    print("Tuple :", sample_tuple)
    print("Minimum value :", min(sample_tuple))
    print("Maximum value :", max(sample_tuple))


if __name__ == '__main__':
    sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
    duplicates_remove(sample_list)
