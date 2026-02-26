"""
Task - 14: Find the factors of a number, optimize it as much as you can.
"""

# import sqrt function from math module 
from math import sqrt

# define function to get factors of a number
def get_factors(number):
    factor_list = []

    for i in range(1, int(sqrt(number)) + 1):
        if number%i == 0:
            factor_element = int(number/i)

            if factor_element != i:
                factor_list.append(factor_element)
                factor_list.append(i)
            else:
                factor_list.append(factor_element)

    return sorted(factor_list)

# take input from user and validate it
while True:
    try:
        number = int(input("\nEnter number to find their factors: "))

        if number < 0:
            number = abs(number)
            
            # call the function to get factors
            result = get_factors(number)

            for i in range(len(result)):
                result.append(-(result[i]))

            print(f"\nFactors of {number}: {sorted(result)}")
            
            break
        else:
            # call the function to get factors
            result = get_factors(number)
            print(f"\nFactors of {number}: {result}")  
            
            break  
    except ValueError:
        print("\nValueError: Enter valid integer input only.")
    except Exception:
        print("\nPlease enter valid integer input only.")