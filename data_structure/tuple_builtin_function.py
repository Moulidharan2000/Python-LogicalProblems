def built_func(sampl_tuple):
    count_value = sampl_tuple.count(3)
    print("count element 3 using count method : ", count_value)

    index_value = sampl_tuple.index(4)
    print("Index value of element 4 : ", index_value)

    add = sum(sampl_tuple)
    print("sum of elements in tuple : ", add)

    sample_tuple2 = sorted(sampl_tuple)
    print("sorted tuple : ", sample_tuple2)

    maximum = max(sampl_tuple)
    print("maximum value in tuple : ", maximum)


if __name__ == "__main__":
    sample_tuple = (1, 3, 2, 4, 6, 5, 3, 3, 7, 3)
    built_func(sample_tuple)
