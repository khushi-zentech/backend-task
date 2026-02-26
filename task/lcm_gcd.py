"""
Task - 15: Find LCM and GCD of a number.
"""

# define function to find GCD
def find_gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    
    return num1

# define function to find LCM
def find_lcm(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    
    lcm = (num1 * num2) // find_gcd(num1, num2)
    return lcm

# take input from user and validate it
while True:
    try:
        num1 = int(input("\nEnter first number: "))
        num2 = int(input("\nEnter second number: "))

        if num1 < 0 or num2 < 0:
            print("\nPlease enter positive integers only.")
            continue

        # call the functions
        lcm_result = find_lcm(num1, num2)
        gcd_result = find_gcd(num1, num2)

        # display results
        print(f"\nGCD of {num1} and {num2}: {gcd_result}")
        print(f"LCM of {num1} and {num2}: {lcm_result}")
        
        break
    except ValueError:
        print("\nValueError: Enter valid integer input only.")
    except Exception:
        print("\nPlease enter valid integer input only.")