"""
Derrick Hobbs
3/28/2023
SDEV300
This is a Math and Secret Generation program
"""

import math
import datetime

#function for password
def generate_secure_password():
    import random
    import string

    password_length = 12
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    password_characters = [random.choice(letters + digits + special_chars) for _ in range(password_length)]
    random.shuffle(password_characters)
    password = ''.join(password_characters)
    return password

#function for percentage
def calculate_percentage():
    while True:
        try:
            num = float(input("Enter the number: "))
            percent = float(input("Enter the percentage: "))
            result = num * percent / 100
            print(f"{percent}% of {num} is {result}")
            break
        except ValueError:
            print("Invalid input, please try again.")

#function for days
def days_until_july_4_2025():
    target_date = datetime.date(2025, 7, 4)
    today = datetime.date.today()
    delta = target_date - today
    print(f"There are {delta.days} days until July 4, 2025.")

#function to calculate leg of a triangle
def calculate_leg_of_triangle():
    while True:
        try:
            a = float(input("Enter the length of side a: "))
            b = float(input("Enter the length of side b: "))
            angle_degrees = float(input("Enter the angle in degrees between sides a and b: "))
            angle_radians = math.radians(angle_degrees)
            c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(angle_radians))
            print(f"The length of side c is {c}")
            break
        except ValueError:
            print("Invalid input, please try again.")

#function to calculate volume of a cylinder
def calculate_volume_of_cylinder():
    while True:
        try:
            radius = float(input("Enter the radius of the base: "))
            height = float(input("Enter the height of the cylinder: "))
            volume = math.pi * radius**2 * height
            print(f"The volume of the cylinder is {volume}")
            break
        except ValueError:
            print("Invalid input, please try again.")

#menu choices
while True:
    print("\nMENU")
    print("a. Generate Secure Password")
    print("b. Calculate and Format a Percentage")
    print("c. How many days from today until July 4, 2025?")
    print("d. Use the Law of Cosines to calculate the leg of a triangle")
    print("e. Calculate the volume of a Right Circular Cylinder")
    print("f. Exit program")
    choice = input("Enter your choice (a-f): ")
    if choice == 'a':
        print(f"Your secure password is: {generate_secure_password()}")
    elif choice == 'b':
        calculate_percentage()
    elif choice == 'c':
        days_until_july_4_2025()
    elif choice == 'd':
        calculate_leg_of_triangle()
    elif choice == 'e':
        calculate_volume_of_cylinder()
    elif choice == 'f':
        print("Exiting program.")
        break
    else:
        print("Invalid choice, please try again.")
