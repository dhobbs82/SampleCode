"""
Derrick Hobbs
3/2/2023
SDEV300
This is a voter registration program
"""

import re

def prompt_continue():
    """
    Prompt the user to continue with the registration process
    """
    answer = input("Do you want to continue with the Voter Registration? ")
    return answer.lower() == "yes"

def prompt_first_name():
    """
    Prompt the user for their first name
    """
    first_name = input("What is your first name? ")
    return first_name.strip()

def prompt_last_name():
    """
    Prompt the user for their last name
    """
    last_name = input("What is your last name? ")
    return last_name.strip()

def prompt_age():
    """
    Prompt the user for their age
    """
    while True:
        age_str = input("What is your age? ")
        if not age_str.isdigit():
            print("Please enter a valid age number.")
        else:
            age = int(age_str)
            if age <= 0 or age > 120:
                print("Please enter a valid age number.")
            return age

def prompt_citizenship():
    """
    Prompt the user for their citizenship status
    """
    while True:
        citizenship = input("Are you a U.S. Citizen? ")
        if citizenship.lower() in ["yes", "no"]:
            return citizenship.lower() == "yes"
        print("Please answer with 'Yes' or 'No'.")

def prompt_state():
    """
    Prompt the user for their state of residence
    """
    while True:
        state = input("What state do you live? ")
        if not re.match("^[A-Za-z]{2}$", state):
            print("Please enter a valid 2-letter state code.")
        else:
            return state.upper()

def prompt_zipcode():
    """
    Prompt the user for their zip code
    """
    while True:
        zipcode = input("What is your zipcode? ")
        if not re.match("^\d{5}$", zipcode):
            print("Please enter a valid 5-digit zip code.")
        else:
            return zipcode

def register_voter():
    """
    Run the voter registration process
    """
    print("Welcome to the Python Voter Registration Application.")
    if prompt_continue():
        first_name = prompt_first_name()
        if prompt_continue():
            last_name = prompt_last_name()
            if prompt_continue():
                age = prompt_age()
                if age >= 18 and prompt_continue():
                    is_citizen = prompt_citizenship()
                    if is_citizen and prompt_continue():
                        state = prompt_state()
                        if prompt_continue():
                            zipcode = prompt_zipcode()
                            print("Thanks for registering to vote. Here is the information we received:")
                            print(f"Name (first last): {first_name} {last_name}")
                            print(f"Age: {age}")
                            print(f"U.S. Citizen: {is_citizen}")
                            print(f"State: {state}")
                            print(f"Zipcode: {zipcode}")
                            print("Thanks for trying the Voter Registration Application. Your voter registration card should be shipped within 3 weeks.")
    else:
        print("Thank you for visiting the Voter Registration Application.")

if __name__ == "__main__":
    register_voter()
