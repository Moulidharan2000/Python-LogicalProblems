def check_perfect_square(nums):
    i = 2
    while i < nums:
        rem = nums % i
        if i*i == nums:
            return True
        i += 1
    return False


if __name__ == '__main__':
    print(check_perfect_square(25))
    print(check_perfect_square(20))
    print(check_perfect_square(36))
