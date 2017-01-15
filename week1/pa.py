def karatsuba(x, y):
    """ Takes two multiple digit integers and outputs their product"""
    # Handle base case
    if x < 10 or y < 10:
        return x * y

    str_x = str(x)
    str_y = str(y)

    # Define a, b, c and d
    a = int(str_x[:len(str_x)/2])
    b = int(str_x[len(str_x)/2:])
    c = int(str_y[:len(str_y)/2])
    d = int(str_y[len(str_y)/2:])

    # Compute ac, bd and (ad + bc) by recursion
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    adbc = karatsuba(a+b, c+d) - ac - bd

    # Compute product
    product = (ac * (10 ** (2 * (len(str_x) / 2))) +
               adbc * (10 ** (len(str_x) / 2)) +
               bd)

    return product
