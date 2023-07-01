#
# def smallest_element(num_list):
#     # k = int(input("Enter the Number : "))
#     # # num_list.sort()
#     # # print(num_list[k-1])
#     # for i in range(len(num_list)):
#     #     for j in range(len(num_list)):
#     #         if num_list[i] < num_list[j]:
#     #             temp = num_list[i]
#     #             num_list[i] = num_list[j]
#     #             num_list[j] = temp
#     # print(num_list[k-1])
#
#     print(num_list[1: len(num_list): 2])
#
#
# if __name__ == '__main__':
#     smallest_element([7, 4, 6, 3, 9, 1])
#     #smallest_element([1, 5, 2, 2, 2, 5, 5, 4])


class Sample:
    id = 123

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    @classmethod
    def get_id(cls):
        return cls.id

    @staticmethod
    def display(address):
        return address


student = Sample("Ramesh", 25)
print(student.get_name())
print(Sample.get_id())
print(Sample.display("Bangalore"))
