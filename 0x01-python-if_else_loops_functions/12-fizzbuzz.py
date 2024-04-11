#!/usr/bin/python3
fizz = 0
def fizzbuzz():
  for i in range(1, 100):
      fizz = 3 * i
      print(fizz)
      if fizz == 100:
         break

fizzbuzz()