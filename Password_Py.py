#Python Code
#This program determines whether a password exactly meets certain criteria
#The length must be at least 6, and no more than 15, lengths
#It must contain at least 1 alphabetic character and 1 digit
#It must not include any spaces


#Developer: Derrick Hobbs CMIS102  Date: 09/25/2022


#Call the main function------------------------------------

def main():

    #display welcome message
    welcome()
    
    #Prompt for password
    p = input("\nWhat is your password? ")
    
    #call functions to check password parameters
    hasLength(p)            #returns True or False
    hasNumbersLetters(p)    #returns True or False
    noSpaces(p)             #returns True or False
    
   
    #determine if all password criteria is met and display result
    if hasLength(p) == False:
        print("Invalid Length")
    if hasNumbersLetters(p) == False:
        print("Invalid Characters")
    if noSpaces(p) == False:
        print("Contains Spaces")      
    if (hasLength(p) and hasNumbersLetters(p) and noSpaces(p) == True):
        print("\nCongratulations, you have unlocked the program")
    


        
#Functions-------------------------------------------------------------
#Display welcome message
def welcome():
    print("\nPlease create a password to unlock the program")
    print("\tThe password must be between 6 and 15 characters")
    print("\tIt must contain at least 1(one) Letter")
    print("\tIt must contain at least 1(one) Number")
    print("\tIt must NOT contain any spaces")

#Function to check that the password is the proper length   
def hasLength(p):
    if len(p) >= 6 and len(p) <= 15:    #must be between 6 and 15 characters  
        return(True)                    #returns True if so
    else:
        return(False)
    
#Function to check whether it contains the required number of characters/digits        
def hasNumbersLetters(p):
    if any(char.isdigit() for char in p) and any(char.isalpha() for char in p): 
        return(True)                    #if any characters are alpha or digit
    else:                               #returns True if so
        return(False)
        

#Function to verify that it does not contain the prohibited character (space)
def noSpaces(p):
    if " " in (p):                      #if any characters are spaces
        return(False)                   #returns False if so
    else:
        return(True)
        
    
#Execute----------------------------------------------------------------------------
main()
