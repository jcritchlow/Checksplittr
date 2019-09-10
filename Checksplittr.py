# Checksplitter script that will allow you to take the total of a check and the number of people, and return how much each person should pay
# Note that it is designed to round up to the next whole dollar amount since most people don't carry change
    #That feature could be removed by removing the math.ceil from the function

import math

def split_check(total, party_size):
    if party_size <= 1:
        raise ValueError("More than 1 person is required to split the check.")
    return math.ceil(total / party_size)

try:
    total_due = float(input("How much is your check?: "))
    party_size = int(input("How many people are in your party?: "))
    amount_due = split_check(total_due, party_size)
except ValueError as err: 
    print("Oh no! That's not a valid value. Try again...")
    print("({})".format(err))
else:
    print("Each person should pay ${} to split the check evenly.".format(amount_due))