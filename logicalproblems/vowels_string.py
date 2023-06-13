def vowels(str1):
    str_list = list(str1)
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in range(len(str_list)):
        for j in range(len(vowels_list)):
            if str_list[i] == vowels_list[j]:
                print(str_list[i], end=" ")
                count += 1
    print("\nNo. of Vowels : ", count)


if __name__ == '__main__':
    str1 = input("Enter the String : ")
    vowels(str1)
