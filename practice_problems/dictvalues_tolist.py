def dict_to_list(sample_dict):
    sample_list = list()
    for i in sample_dict.values():
        if i not in sample_list:
            sample_list.append(i)
    print(sample_list)


if __name__ == '__main__':
    sample_dict = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44,
                   'Sept': 54}
    dict_to_list(sample_dict)
