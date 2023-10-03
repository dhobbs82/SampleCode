#Name:  Derrick Hobbs
#Class: CMIS102 Week 6 Discussion
#Date:  9/25/2022


#This is a program that accepts a string as input: a pet's name
#analyzes the string to count the number of characters excluding <space>
#includes a string method: count
#determines if my initials, in any case combination, are in the string
#displays the result of analyzing the number of characters
#displays whether my initials are in the string in any case combination



def main():
    #call functions
    welcome()
    name, numLetters = getName()
    displayOutput(name,numLetters)
 
    
    
    
#functions------------------------------------------------------------------------

def welcome():
    #welcome function
    print("\nWelcome to Derrick Hobbs Pet Name Program!")
   

def getName():
    #accepting a string as input
    name = input("\nPlease enter your pet's name: ")
    
    #analyzing a characteristic of the string input
    #including string method: count
    numLetters = len(name) - name.count(" ")

    return(name, numLetters)

        
def displayOutput(name, numLetters):
        #displaying the result of analyzing the string input
        print("\nYour pet's name is",numLetters,"characters long")
        #determining if my initials, in any case combination, are inside the string
        if ('d' in name) == True and ('h' in name) == True:
            print("\nMy initials are in your pet's name :)\n")
        elif('D' in name) == True and ('H' in name) == True:
            print("\nMy initials are in your pet's name :)\n")
        elif('d' in name) == True and ('H' in name) == True:
            print("\nMy initials are in your pet's name :)\n")
        elif('D' in name) == True and ('h' in name) == True:
            print("\nMy initials are in your pet's name :)\n")
        else:
            print("\nMy initials are not in your pet's name :(\n")
        
        
            
#execute---------------------------------------------------------------------------
main()
