
def swap(int_arr):
    temp = 0
    for i in range(len(int_arr)):
        for j in range(len(int_arr)):
            if int_arr[i] < int_arr[j]:
                temp = int_arr[i]
                int_arr[i] = int_arr[j]
                int_arr[j] = temp
    for i in range(len(int_arr)):
        print(int_arr[i], end=" ")


if __name__ == '__main__':
    int_arr = [2, 5, 4, 6, 8, 3, 1, 9, 7]
    print(type(int_arr))
    swap(int_arr)
