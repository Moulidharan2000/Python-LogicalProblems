def products(list1):
    temp = 0
    max_value = max(list1)
    for i in range(len(list1)):
        for j in range(len(list1)):
            temp = list1[i] * list1[j]
            if max_value == list1[i] * temp:
                return True
            else:
                return False


if __name__ == "__main__":
    print(products([2, 8, 4, 1]))
    print(products([-1, -10, 1, -2, 20]))
    print(products([-1, -20, 5, -1, -2, 2]))
