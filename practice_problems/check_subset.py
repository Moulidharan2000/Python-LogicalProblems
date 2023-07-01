def subset_check(first_set, second_set):
    check = first_set.issubset(second_set)
    print("first_set is a subset of second_set : ", check)
    check = first_set.issuperset(second_set)
    print("second_set is a subset of first_set : ", check)

    check = first_set.issuperset(second_set)
    print("first_set is a superset of second_set : ", check)
    check = second_set.issuperset(first_set)
    print("second_set is a superset of first_set : ", check)

    first_set.clear()
    print(first_set)
    print(second_set)


if __name__ == "__main__":
    first_set = {27, 43, 34}
    second_set = {34, 93, 22, 27, 43, 53, 48}
    subset_check(first_set, second_set)
