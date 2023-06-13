str1 = "silent"
str2 = "listen"
if len(str1) == len(str2):
    if sorted(str1) == sorted(str2):
        print("Strings are anagrams")
    else:
        print("Strings are not anagrams")
else:
    print("Strings are not anagrams")