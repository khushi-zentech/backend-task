"""
Task - 14: Find the factors of a number, optimize it as much as you can.
"""

# define function to get factors of a number
def get_factors(number):
    factor_list = []

    for i in range(1, int(number ** 0.5)+1):
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
    number = input("\nEnter number to find their factors: ")

    if number.isdigit():
        # call the function
        result = get_factors(int(number))
        
        print(f"\nFactors of {number}: {result}")
        break
    else:
        print("\nPlease enter a valid integer input only.")