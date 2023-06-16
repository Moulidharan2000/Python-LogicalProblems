def count_words(str_words):
    str_list = list(str_words)
    print(str_list)
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in str_list:
        if i in vowels_list:
            count += 1
    print("Vowels Count in a String :", count)


if __name__ == '__main__':
    str_words = input("Enter the String : ")
    count_words(str_words)
