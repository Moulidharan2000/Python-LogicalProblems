def remove_elements(roll_number, sample_dict):
    # for i in roll_number:
    #     if i not in sample_dict.values():
    #         roll_number.remove(i)
    roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
    print(roll_number)


if __name__ == "__main__":
    roll_number = [47, 64, 69, 37, 76, 83, 97]
    sample_dict = {'Jon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}
    remove_elements(roll_number, sample_dict)