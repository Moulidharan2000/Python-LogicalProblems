import array as arr

a = arr.array('i', [1, 2, 3, 4, 5])
i = len(a) - 1
while i >= 0:
    print(a[i], end=" ")
    i -= 1
