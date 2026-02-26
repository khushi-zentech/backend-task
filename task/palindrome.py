"""
Task - 10: Find whether a given number is a palindrome or not ?
"""

# define function to get reverse of given number
def find_reverse(number):
    rev_num = 0

    while number > 0:
        digit = number%10
        rev_num = (rev_num*10) + digit
        number = number//10

    return rev_num

# define function to check whether given number is palindrome or not
def check_palindrome():
    while True:
       
        try:
            # get user input
            number = int(input("\nEnter Number: "))

            if number < 0:
                print("\nPalindrome number of negative integer does not exist.")
                continue

            # call function to get reverse of given number
            reverse = find_reverse(number)

            # display output
            print(f"\nYour given number: {number}")
            print(f"Reverse of that number: {reverse}")

            # check condition for palindrome number and display the result
            if reverse == number:
                print("\nYes, given number is a Palindrome Number.")
            else:
                print("\nNo, given number is not a Palindrome Number.")

            break
        except Exception:
            print("\nPlease enter valid integer input only.")

# call the function
check_palindrome()