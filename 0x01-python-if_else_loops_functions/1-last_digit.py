#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# number = -4323
lastDigit = number % 10
if (lastDigit) > 5:
  print("Last digit of", number, "is", lastDigit, "and is greater than 5")
elif lastDigit == 0:  
  print("Last digit of", number, "is", lastDigit * -1, "and is 0")
else:
    print("Last digit of", number, "is", lastDigit, "and is less than 6 and not 0")



# import random

# Generate a random number //
# number = random.randint(-10000, 10000) 

# Get the last digit of the number // 
# last_digit = number % 10

# Print the last digit //
# if last_digit > 0:
#   print(f"The last digit of {number} is {last_digit}")
# elif last_digit < 0:
#   print(f"The last digit of {number} is {last_digit * -1}")
# else:
#   print(f"The last digit of {number} is {last_digit}")