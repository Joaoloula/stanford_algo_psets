def karatsuba(x, y):
    """ Takes two multiple digit integers and outputs their product"""
    # Handle base case
    if x < 10 and y < 10:
        return x * y

    str_x = str(x)
    str_y = str(y)
    len_x = len(str_x)
    len_y = len(str_y)

    if len_x > len_y:
        str_y = '0'*(len_x - len_y) + str_y
        len_y = len_x

    elif len_x < len_y:
        str_x = '0'*(len_y - len_x) + str_x
        len_x = len_y

    # Define a, b, c and d
    a = int(str_x[:len_x/2])
    b = int(str_x[len_x/2:])
    c = int(str_y[:len_y/2])
    d = int(str_y[len_y/2:])

    # Compute ac, bd and (ad + bc) by recursion
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    adbc = karatsuba(a+b, c+d) - ac - bd

    # Compute product
    product = (ac * (10 ** ((len(str_x)))) +
               adbc * (10 ** ((len(str_x) + 1)/ 2)) +
               bd)

    return product
