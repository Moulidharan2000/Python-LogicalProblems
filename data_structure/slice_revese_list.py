def reverse_list(num_list):
    global list_chunk
    length = len(num_list)
    chunk_size = int(length / 3)
    start = 0
    end = length
    for i in range(length):
        index = slice(start, end)
        list_chunk = num_list[index]
    print("After reversing : ", list(reversed(list_chunk)))
    start = end
    end += length


if __name__ == '__main__':
    num_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    print("Origin List : ", num_list)
    reverse_list(num_list)