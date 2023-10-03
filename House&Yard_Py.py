#Python Code
#This program will calculate and display how much it costs to clean a house or do yard service
#Yard service involves mowing, edging, and shrub pruning
#House cleaning is based on number of rooms and level of cleaning


#Developer: Derrick Hobbs CMIS102  Date: 10/09/2022

#Display welcome message function--------------------------------------------------------------------------------------------------------------------------------------
def Welcome():
    print("\nWelcome to Derrick's House Cleaning and Yard Service")
    print("-----------------------------------------------------")
    print("\nWe base the cost of House Cleaning on how Big your house is")
    print("and what Type of Cleaning you want")
    print("\nWe base the cost of Yard Service on Mowing, Edging, and Shrub Pruning")
    print("\nSeniors receive a $50 discount")
    print("\nUse my Estimator for a Free Quote!\n")
    print("------------------------------------------------------")
    
#Asking the customer whether they are requesting house cleaning or yard services function------------------------------------------------------------------------------
def get_choice():

    choices = ['Yard', 'yard', 'House', 'house']            #Setting valid user inputs
    choice = None                                           #Initializing
    while choice not in choices:                            #While invalid input, reprompt until valid
        print("\n What type of service would you like?")        #Ask for type of service
        choice = input(" Type 'Yard' or 'House' :\t")           #Prompt for proper input
    return (choice)                                         #Storing variable choice as to yard or house

#Asking the customer if they are a senior citizen function-------------------------------------------------------------------------------------------------------------
def get_discount():

    seniors = ['Yes', 'yes', 'No', 'no']                    #Setting valid user inputs
    senior = None                                           #Initializing
    while senior not in seniors:                            #While invalid input, reprompt until valid
        print("\n Are you a senior citizen?")                   #Ask for senior status
        senior = input(" Type 'Yes' or 'No' :\t")               #Prompt for proper input
    return (senior)                                         #Storing variable senior to determine discount

#Get square footage of yard for mowing function------------------------------------------------------------------------------------------------------------------------
def get_mowing():
    
    sqft = input("\n Enter your yard's square footage :\t")         #Prompt for square footage
    while not sqft.isdigit() or int(sqft) == 0:                     #While input is not a digit, or is = 0, reprompt until valid            
        print(" Invalid: Enter a number")                               #Print directions
        sqft = input("\n Enter your yard's square footage :\t")         #Prompt for proper input
    return (sqft)                                                   #Storing variable sqft of mowing to use in yard calculation

#Get linear footage of yard's edges for edging function----------------------------------------------------------------------------------------------------------------
def get_edging():
    
    Lnft = input("\n Enter the linear footage of your yard's edges :\t")        #Prompting for linear footage
    while not Lnft.isdigit() or int(Lnft) == 0:                                 #While input is not a digit, or is = 0, reprompt until valid
        print(" Invalid: Enter a number")                                           #Print directions
        Lnft = input("\n Enter the linear footage of your yard's edges :\t")        #Prompt for proper input
    return (Lnft)                                                               #Storing variable lnft of edges to use in yard calculation

#Get how many shrubs need pruning function-----------------------------------------------------------------------------------------------------------------------------

def get_shrubs():
    
    shrb = input("\n Enter number of shrubs :\t")           #Prompt for number of shrubs
    while not shrb.isdigit():                               #While input is not a digit, reprompt until valid
        print(" Invalid: Enter a number")                       #Print directions
        shrb = input("\n Enter number of shrubs :\t")           #Prompt for proper input
    return (shrb)                                           #Storing variable shrub as number of shrubs in yard calculation

#Calculate the cost of yard service based on mowing, edging and shrub pruning function---------------------------------------------------------------------------------

def yard_calculation(sqft,Lnft,shrb):

    z = (int(sqft) + int(Lnft) + (int(shrb) * 5))               #Calculation for yard services = ($1 per sqft)+($1 per Lnft)+($5 per shrb)
    return (z)                                                  #Storing variable result of adding together the cost of the 3 services

#Display the yard service output function------------------------------------------------------------------------------------------------------------------------------

def yard_display(z):
    
    print('\nThe total cost will be $',z,'for Yard Service')    #Print output of the yard service cost calculation

#Get number of rooms function------------------------------------------------------------------------------------------------------------------------------------------

def get_rooms():
     
    houseSize = input("\n How many rooms are in your house?\t")     #Prompt for number of rooms
    while not houseSize.isdigit() or int(houseSize) == 0:           #While input is not a digit, or = 0, reprompt until valid
        print(" Invalid: Enter a number of rooms")                      #Print directions
        houseSize = input("\n How many rooms are in your house? ")      #Prompt for proper input    
    return (houseSize)                                              #Storing variable of how many rooms are in the house for calculation

#Get type of cleaning function-----------------------------------------------------------------------------------------------------------------------------------------

def get_clean():
    
    levelCleans = ['1', '2']                                                                    #Setting valid user inputs
    levelClean = None                                                                           #Initializing
    while levelClean not in levelCleans:                                                        #While invalid input, reprompt until valid
        levelClean = input("\n Please enter 1 for Deep Clean or 2 for Extra Deep Clean :\t ")       #Prompt for proper input
    return (levelClean)                                                                         #Storing variable type of cleaning for house calculation

#Calculate the cost of cleaning based on rooms and level of cleaning function------------------------------------------------------------------------------------------

def house_calculation(houseSize,levelClean):
    
    x = (int(houseSize) * int(levelClean))              #2 times Surcharge for Extra Deep Clean
    return (x)                                          #Storing variable result of multiplying number of rooms by one for deep clean, or two for extra deep clean

#Display the house cleaning output function----------------------------------------------------------------------------------------------------------------------------

def house_display(x):
    
    print('\nThe total cost will be $',x,'for House Cleaning')         #Print output of the house cleaning cost calculation

#Call main function----------------------------------------------------------------------------------------------------------------------------------------------------
    
def main():
    
    Welcome()                                                           #Call Welcome message    
    choice = get_choice()                                               #Call choice function
    while choice == 'house' or choice == 'House':                       #While choice is 'House'...
        houseSize = get_rooms()                                             #Call Number of rooms function    
        levelClean = get_clean()                                            #Call Level of clean function                                                                       
        if houseSize == 1:                                                  #Small house is 1 room 
            cost = 100                                                          #Cost $100
        elif houseSize == 2:                                                #Medium house is 2 rooms
            cost = 110                                                          #Cost $110 per room
        elif houseSize == 3:                                                #Large house is 3 rooms 
            cost = 120                                                          #Cost $120 per room
        else:                                                               #Any other number higher than 3 rooms and not zero...
            cost = 120                                                          #Cost $120 per room                                     
        senior = get_discount()                                             #Call function for senior discount within House choice
        while senior == 'No' or senior == 'no':                             #While no senior discount...
            x = house_calculation(houseSize,levelClean)*cost + 175              #Call function for house cleaning calculation
            house_display(x)                                                    #Display output
            break                                                               #Break senior 'No' loop
        while senior == 'Yes' or senior == 'yes':                           #While applying senior discount...
            x = house_calculation(houseSize,levelClean)*cost  + 125             #Call function for house cleaning calculation, 50 dollars less for senior discount
            house_display(x)                                                    #Display output
            break                                                               #Break senior 'Yes' loop
        break                                                               #Break choice House loop        
    while choice == 'yard' or choice == 'Yard':                         #While choice is 'Yard'...
        sqft = get_mowing()                                                 #Call Mowing function
        Lnft = get_edging()                                                 #Call Edging function
        shrb = get_shrubs()                                                 #Call Shrub function
        senior = get_discount()                                             #Call function for senior discount within Yard choice
        while senior == 'No' or senior == 'no':                             #While no senior discount...
            z = yard_calculation(sqft,Lnft,shrb) + 175                          #Call function for yard services calculation                               
            yard_display(z)                                                     #Display output
            break                                                               #Break senior 'No' loop
        while senior == 'Yes' or senior == 'yes':                           #While applying senior discount...
            z = yard_calculation(sqft,Lnft,shrb) + 125                          #Call function for yard services calculation, 50 dollars less for senior discount
            yard_display(z)                                                     #Display output
            break                                                               #Break senior 'Yes' loop
        break                                                               #Break choice Yard loop
        
    
    

#Execute---------------------------------------------------------------------------------------------------------------------------------------------------------------
main()
    
    
    

    






