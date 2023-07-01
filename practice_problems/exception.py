try:
    a = 20
    b = 0
    c = a / b
    print(c)
except Exception as exception:
    print(exception)

try:
    nums_list = [2, 1, 4, 5]
    print(nums_list[6])
except IndexError:
    print("Index out of bound...")
finally:
    print("Final Block")

print("\n")


class InvalidAgeException(Exception):
    def __str__(self):
        return "Invalid Age"


class Age:
    valid_age = 18
    try:
        person_age = int(input("Enter the Age : "))
        if person_age < valid_age:
            raise InvalidAgeException
        else:
            print("Valid Age...")
    except Exception as invalid:
        print(invalid)


print("\n")


class MyCustomException(Exception):
    pass


def sample_():
    try:
        a = 10
        b = 20
        if b == 20:
            raise MyCustomException('b is 20')
    except MyCustomException as ex:
        print('custom exception block', ex)
    except Exception as ex:
        print(ex)
    finally:
        print('completed')


if __name__ == '__main__':
    sample_()
