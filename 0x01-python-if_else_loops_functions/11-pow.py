#!/usr/bin/python3
base = 98
exponent = 90
power = 1
expo = exponent

if exponent > 0:
    while exponent != 0:
        power = base * base
        exponent = exponent - 1

print(base," to the power of ",expo," is ",power)



