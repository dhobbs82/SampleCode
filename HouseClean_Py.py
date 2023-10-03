#Python Code
#This program will calculate and display how much cost to clean a house
#User will be prompted for number of rooms in their house
#User will be prompted for the type of cleaning they want


#Developer: Derrick Hobbs CMIS102  Date: 09/06/2022

def main():
    #Initialize variables
    floorClean = 25     #25 as the cost to clean floors (1)
    windClean = 20      #20 as the cost to clean windows (2)
    priceLg = 200      #200 for a large house 4+ rooms
    priceMed = 180     #180 for a medium house 3 rooms
    priceSm = 170      #170 for a small house 2 rooms
    
    #Display welcome message
    print("\nWelcome to Derrick's Cleaning Service")
    print("-------------------------------------")
    print("\nWe base the cost on how big your house is, and what type of cleaning you want")
    print("\nUse my House Cleaning Estimator for a Free Quote!")
    print("-------------------------------------------------")

    #Prompt for number of rooms
    houseSize = int(input("\n How many rooms are in your house? "))


    #Validate the input
    if houseSize <= 1: #we wont clean a house with 1 room
        print(" Invalid too small")
        houseSize = int(input("\n How many rooms are in your house? "))

    
    if houseSize == 2: #cutoff for small house is 2 rooms
        print("\n\t It will cost a base of $ 170 for your small house \n")
    elif houseSize == 3: #cutoff for medium house is 3 rooms
        print("\n\t It will cost a base of $ 180 for your medium house \n")
    elif houseSize >= 4: #cutoff for large house is 4+ rooms
        print("\n\t It will cost a base of $ 200 for your large house \n")
    

        

    #Prompt for the type of cleaning
    typeClean = int(input(" What type of cleaning would you like (1 for Floors, 2 for Windows)? "))

    #Validate the input
    if typeClean != 1:
        if typeClean != 2:
            print("\n Please enter 1 for Floors or 2 for Windows ")
            typeClean = int(input("\n What type of cleaning would you like? "))
            
    #Calculate and Display the cost of cleaning based on number of rooms and type of cleaning
    if houseSize == 2 and typeClean == 1:
        print("\n\t The total cost will be $",priceSm+(houseSize*floorClean),"to clean your house")
    elif houseSize == 2 and typeClean == 2:
        print("\n\t The total cost will be $",priceSm+(houseSize*windClean),"to clean your house")
    elif houseSize == 3 and typeClean == 1:
        print("\n\t The total cost will be $",priceMed+(houseSize*floorClean),"to clean your house")
    elif houseSize == 3 and typeClean == 2:
        print("\n\t The total cost will be $",priceMed+(houseSize*windClean),"to clean your house")
    elif houseSize >= 4 and typeClean == 1:
        print("\n\t The total cost will be $",priceLg+(houseSize*floorClean),"to clean your house")
    elif houseSize >= 4 and typeClean == 2:
        print("\n\t The total cost will be $",priceLg+(houseSize*windClean),"to clean your house")

    

    #Execute-----------------------------------------------------------------
main()
    
    
    

    
                    
