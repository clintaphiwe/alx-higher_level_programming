#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    #Handle tuple_a
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0 
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0

    #Handle tuple_b
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0

    #Return the result tuple
    result = (a1 + b1, a2 + b2)
    print(result)

# e = 88, 0
# z = 43, 67
# add_tuple(e, z)
tuple_a = (1, 89)

print(add_tuple(tuple_a, (1, )))