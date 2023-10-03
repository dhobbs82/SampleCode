"""
Derrick Hobbs
4/18/2023
SDEV300
This is a Population Change and Housing program
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define a function to get user input and validate it
def get_user_input(choices):
    """
    This function takes a list of valid choices as input and prompts the user for input until a valid choice is entered.
    """
    while True:
        choice = input()
        if choice not in choices:
            print("Invalid input, please enter", ", ".join(choices))
        else:
            return choice

# Load the population change and housing data
pop_change = pd.read_csv("PopChange.csv")
housing = pd.read_csv("Housing.csv")

# Define the columns we want to analyze for each dataset
pop_cols = ["Pop Apr 1", "Pop Jul 1", "Change Pop"]
housing_cols = ["AGE", "BEDRMS", "BUILT", "ROOMS", "UTILITY"]

# Define a function to perform histogram analysis and plot for a given column
def analyze_column(df, col):
    """
    This function takes a DataFrame and a column name as input and performs histogram analysis and plot for the column.
    """
    # Get the column data and remove NaN values
    data = df[col].dropna()
    # Calculate statistics
    count = data.count()
    mean = np.mean(data)
    std = np.std(data)
    minimum = np.min(data)
    maximum = np.max(data)
    # Print statistics
    print("Count =", count)
    print("Mean =", mean)
    print("Standard Deviation =", std)
    print("Min =", minimum)
    print("Max =", maximum)
    # Plot histogram
    plt.hist(data, bins=10)
    plt.title(col)
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()

# Define a function to perform analysis on a given dataset
def analyze_dataset(df, cols):
    """
    This function takes a DataFrame and a list of column names as input and performs analysis on each column.
    """
    while True:
        # Print column menu
        print("Select the Column you want to analyze:")
        for i, col in enumerate(cols):
            print(chr(ord('a') + i) + ".", col)
        print("d. Exit Column")
        # Get user input and validate it
        choices = [chr(ord('a') + i) for i in range(len(cols))] + ['d']
        choice = get_user_input(choices)
        # Exit column menu if chosen
        if choice == 'd':
            break
        # Analyze column if valid choice
        col = cols[ord(choice) - ord('a')]
        print("You selected", col)
        analyze_column(df, col)

while True:
    # Print main menu
    print("***************** Welcome to the Python Data Analysis App**********")
    print("Select the file you want to analyze:")
    print("1. Population Data")
    print("2. Housing Data")
    print("3. Exit the Program") 
    # Get user input and validate it
    choices = ['1', '2', '3']
    choice = get_user_input(choices)
    # Exit program if chosen
    if choice == '3':
        print("*************** Thanks for using the Data Analysis App**********")
        break
    # Analyze dataset if valid choice
    if choice == '1':
        print("You have entered Population Data.")
        analyze_dataset(pop_change, pop_cols)
    elif choice == '2':
        print("You have entered Housing Data.")
        analyze_dataset(housing, housing_cols)
