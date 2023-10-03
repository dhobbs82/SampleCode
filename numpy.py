"""
Derrick Hobbs
4/11/2023
SDEV300
This is a program to demonstrate numpy
"""

import re
import numpy as np

# function to validate phone number
def validate_phone_number(phone_number):
    pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    return pattern.match(phone_number)

# function to validate zip code
def validate_zip_code(zip_code):
    pattern = re.compile(r'^\d{5}-\d{4}$')
    return pattern.match(zip_code)

# function to get user input for matrices
def get_matrix_input():
    matrix = []
    for i in range(3):
        row = input(f"Enter three comma-separated values for row {i+1}: ")
        row_values = row.split(',')
        # check that each value is numeric
        if not all(map(lambda x: x.isnumeric(), row_values)):
            print("Error: Matrix values must be numeric.")
            return None
        matrix.append([int(x) for x in row_values])
    return matrix

# main program loop
while True:
    # get user input for phone number and zip code
    phone_number = input("Enter your phone number in the format ###-###-####: ")
    if not validate_phone_number(phone_number):
        print("Error: Invalid phone number format.")
        continue
    zip_code = input("Enter your zip code in the format #####-####: ")
    if not validate_zip_code(zip_code):
        print("Error: Invalid zip code format.")
        continue
    
    # get user input for matrices
    print("Enter values for matrix A:")
    matrix_a = get_matrix_input()
    if matrix_a is None:
        continue
    print("Enter values for matrix B:")
    matrix_b = get_matrix_input()
    if matrix_b is None:
        continue
    
    # get user input for operation
    operation = input("Enter the operation to perform (+, -, *, matmul): ")
    if operation not in ['+', '-', '*', 'matmul']:
        print("Error: Invalid operation.")
        continue
    
    # perform matrix operation
    if operation == '+':
        result = np.add(matrix_a, matrix_b)
    elif operation == '-':
        result = np.subtract(matrix_a, matrix_b)
    elif operation == '*':
        result = np.multiply(matrix_a, matrix_b)
    elif operation == 'matmul':
        result = np.matmul(matrix_a, matrix_b)
    
    # print results
    print("Result:")
    print(result)
    print("Transpose:")
    print(result.T)
    print("Mean of rows:")
    print(np.mean(result, axis=1))
    print("Mean of columns:")
    print(np.mean(result, axis=0))
    
    # ask if user wants to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != 'y':
        break
