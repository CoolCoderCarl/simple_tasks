user_info = input("Input your data: ")
print(user_info)


print('Hello, {}!'.format('UserName'))


with open("filename") as f:
    print(f.readlines())


def sum_2(a, b):
    """
    Sum of two digits
    :param a:
    :param b:
    :return:
    """
    c = a + b
    return c


def print_all(*args):
    """
    Print all arguments
    :param args:
    :return:
    """
    for i in args:
        print(i)


# Variable for with_global()
a = 10
b = 20


def with_global():
    """
    Use the global var
    :return:
    """
    global a
    b = 2
    c = a + b
    print(c)
