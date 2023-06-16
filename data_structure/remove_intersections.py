def remove_intersect(first_set, second_set):
    third_set = set(first_set.intersection(second_set))
    print(third_set)
    for i in third_set:
        first_set.remove(i)
        second_set.remove(i)
    print("After remove intersection in first_set : ", first_set, "\n", "After remove intersection in second_set : ", second_set)


if __name__ == '__main__':
    first_set = {23, 42, 65, 57, 78, 83, 29}
    second_set = {57, 83, 29, 67, 73, 43, 48}
    remove_intersect(first_set, second_set)