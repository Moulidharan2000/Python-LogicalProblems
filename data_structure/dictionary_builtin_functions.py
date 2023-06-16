def dic_functions(sample_dic):
    element = sample_dic.values()
    print("Values in dictionary : ", element)

    keys = sample_dic.keys()
    print("Keys in the dictionary : ", keys)

    sample_dic.update({6: 9})
    print("Update dictionary : ", sample_dic)

    sample_dic.popitem()
    print("Pop last item : ", sample_dic)

    sample_dic.pop(3)
    print("Pop item : ", sample_dic)

    sample_dic.setdefault(2)
    print("setdefault function : ", sample_dic)

    items = sample_dic.items()
    print("items in dictionary : ", items)

    specific_key = sample_dic.get(5)
    print("Get specific key : ", specific_key)

    sample_dic2 = {7, 8, 9}
    x = 1
    specific = sample_dic.fromkeys(sample_dic2, x)
    print("Specific key value pairs : ", specific)

    sample_dic.copy()
    print("Copy of dictionary : ", sample_dic)

    sample_dic.clear()
    print("Clear dictionary : ", sample_dic)


if __name__ == "__main__":
    sample_dic = {1: 4, 2: 3, 3: 5, 4: 6, 5: 8}
    dic_functions(sample_dic)