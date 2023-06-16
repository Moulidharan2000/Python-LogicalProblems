def built_fun(sample_set):
    sample_set.add(6)
    print("Add function : ", sample_set)

    sample_set.copy()
    print("Copy function : ", sample_set)

    sample_set2 = {3, 5, 6, 8}
    sample_set.difference(sample_set2)
    print("Difference function : ", sample_set)

    sample_set.difference_update(sample_set2)
    print("Difference_update function : ", sample_set)

    sample_set3 = {10, 12, 11}
    sample_set.update(sample_set3)
    print("update function : ", sample_set)

    sample_set.discard(6)
    print("Discard function : ", sample_set)

    sample_set.intersection(sample_set2)
    print("Intersection function : ", sample_set)

    sample_set2.intersection_update(sample_set)
    print("Intersection_update : ", sample_set2)

    sample_set.isdisjoint(sample_set2)
    print("isdisjoint function : ", sample_set)

    sample_set.issubset(sample_set2)
    print("issubset function : ", sample_set)

    sample_set.pop()
    print("pop function : ", sample_set)

    sample_set.remove(2)
    print("remove function : ", sample_set)

    sample_set.symmetric_difference(sample_set2)
    print("symmetric_difference : ", sample_set)

    sample_set.symmetric_difference_update(sample_set2)
    print("symmetric_difference_update : ", sample_set)

    sample_set.union(sample_set2)
    print("union function : ", sample_set)

    sample_set.clear()
    print("Clear function : ", sample_set)


if __name__ == '__main__':
    sample_set = {4, 5, 2, 3, 1}
    built_fun(sample_set)
