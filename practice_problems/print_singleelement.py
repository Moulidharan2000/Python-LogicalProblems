def single_value(nums):
    a = 0
    for i in nums:
        for j in nums:
            if i != j:
                a = i
    print(a)


if __name__ == '__main__':
    single_value([2, 2, 1])
    single_value([4, 1, 2, 1, 2])
