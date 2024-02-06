# # Write a Python program that provides five utility functions.
# # The program should use a while loop to display these utilities,
# # take user input to choose one, execute the chosen utility function,
# # and continue until the user decides to exit.
# # Utility Functions:
# # Generate Password:
# # Check Valid Username:
# # Check Valid Email Address:
# # Play Number Guessing Game:
# # Calculator:

import random
import string
#~~~~~~~~~~~~~~~~~~~~Password Generator~~~~~~~~~~~~~~~~~~~~
def generate_random_password():
    lc = list('abcdefghijklmnopqrstuvwxyz')
    uc = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    n = list('0123456789')
    sc = list('!@#$%&*()')
    tc = list('!@#$%&*()0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    c1 = random.choice(lc)
    n1 = random.choice(n)
    sc1 = random.choice(sc)
    all0 = random.choice(tc)
    all1 = random.choice(tc)
    all2 = random.choice(tc)
    all3 = random.choice(tc)
    all4 = random.choice(tc)
    total = c1 + n1 + sc1 + all0 + all1 + all2 + all3 + all4
    total = list(total)
    random.shuffle(total)
    total = ''.join(total)
    return total[:8]

#~~~~~~~~~~~~~~~~~~~~Username Checker~~~~~~~~~~~~~~~~~~~~
def is_valid_username(username):
    return len(username) >= 8 and not username[0].isdigit()

#~~~~~~~~~~~~~~~~~~~~Number Guessing Game~~~~~~~~~~~~~~~~~~~~
def number_guessing_game():
    flag = "red"
    while flag == "red":
        lucky_number = random.randrange(1, 11)
        input_value = int(input("Please guess a number between (1-10): "))
        if input_value == lucky_number:
            print("Congratulations! Your guess is correct.")
            flag = "green"
        else:
            print("Please try again")

# ~~~~~~~~~~~~~~~~~~~~Calculator~~~~~~~~~~~~~~~~~~~~
def calculator(operator, o1, o2):
    if operator=='+':
        r=o1+o2
    elif operator=='-':
        r=o1-o2
    elif operator=='*':
        r=o1*o2
    elif operator=='/':
        r=o1/o2
    else:
        return "Invalid Operand"
    return r

#~~~~~~~~~~~~~~~~~~~~Email Checker~~~~~~~~~~~~~~~~~~~~
def valid_email(email):
    index1 = email.find('@')
    index2 = email.find('.')
    if index1 != -1 and index2 != -1 and index1 < index2:
        user = email[:index1]
        return is_valid_username(user)
    return False
# Running Commands Below
while True:
    print("Choose A Utility Function:")
    print("1) Generate Random Password")
    print("2) Check Valid Username")
    print("3) Check Valid Email Address")
    print("4) Number Guessing Game")
    print("5) Calculator")
    fc = input("Enter your choice (1-5): ")
    if fc== '1':
        random_password = generate_random_password()
        print("Random Password:", random_password)
    elif fc == '2':
        username_to_check = input("Enter a username: ")
        if is_valid_username(username_to_check):
            print(f"The username {username_to_check} is valid.")
        else:
            print(f"The username {username_to_check} is not valid.")
    elif fc == '3':
        email_to_check = input("Enter the email address to check: ")
        if valid_email(email_to_check):
            print("Your Email Address Is Valid")
        else:
            print("Your Email Address Is Invalid")
    elif fc == '4':
        number_guessing_game()
    elif fc == '5':
        operator_input = input("Enter operator (+, -, *, /): ")
        o1_input = float(input("Enter the first operand: "))
        o2_input = float(input("Enter the second operand: "))
        result = calculator(operator_input, o1_input, o2_input)
        print(f"Result: {result}")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
    continue_choice = input("Do you want to continue? (yes/no): ")
    if continue_choice != 'yes' or continue_choice != 'Yes' or continue_choice != 'YES' :
        print("Thankyou for using!")
        # break


