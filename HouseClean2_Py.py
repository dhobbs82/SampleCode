#Python Code
#This program will calculate and display how much cost to clean a house
#User will be prompted for number of rooms in their house
#User will be prompted for level of cleanliness


#Developer: Derrick Hobbs CMIS102  Date: 09/11/2022

#Display welcome message----------------------------------------------------------
def Welcome():
    print("\nWelcome to Derrick's Cleaning Service")
    print("-------------------------------------")
    print("\nWe base the cost on how big your house is, and what type of cleaning you want")
    print("\nUse my House Cleaning Estimator for a Free Quote!")
    print("-------------------------------------------------")

#Get number of rooms-------------------------------------------------------------
def GetNumRoomsInput():
        
    houseSize = int(input("\n How many rooms are in your house? "))
    
     
    #Validate the input
    if houseSize <= 1: #we wont clean a house with 1 room
        print(" Invalid too small")
        houseSize = int(input("\n How many rooms are in your house? "))
    

    return (houseSize)

#Get type of cleaning------------------------------------------------------------
def GetTypeCleanInput():  

    levelClean = int(input(" Please enter 1 for Deep Clean, 2 for Extra Deep Clean "))

    #Validate the input
    if levelClean != 1:
        if levelClean != 2:
            print("\n Please enter 1 for Deep Clean or 2 for Extra Deep Clean ")
            levelClean = int(input("\n What type of cleaning would you like? "))

    return (levelClean)

#Calculate the cost of cleaning based on rooms and level of cleaning--------------
def Calculation(houseSize,levelClean):
    
    x = (houseSize * levelClean) #2 times Surcharge for Extra Deep Clean

    return (x)

#Display the output---------------------------------------------------------------
def Display(x):
    print('\nThe total cost will be $',x,'to clean your house')

#Call the main function-----------------------------------------------------------
def main():
    #Call welcome message
    Welcome()
    #Get Number of rooms
    houseSize = GetNumRoomsInput()
    #Get Level of clean
    levelClean = GetTypeCleanInput()
    #Price based on house size
    if (houseSize == 2):  #small house is 2 rooms, cost 170 per room
        cost = 170          
    elif (houseSize == 3): #medium house is 3 rooms, cost 180 per room
        cost = 180
    elif (houseSize >= 4): #large house is 4+ rooms, cost 200 per room
        cost = 200
    else:
        cost = 0
    #Calculate the total cost    
    x = Calculation(houseSize,levelClean)*cost
    #Display output
    Display(x)
    
    
    

    #Execute-----------------------------------------------------------------
main()
    
    
    

    
                    
