#Name:  Derrick Hobbs
#Class: CMIS102 Week 5 Discussion
#Date:  9/18/2022


#This is a program that finds total passing yards
#User will be prompted for each input of passing yards
#User will decide how many weeks
#Output will be calculated and displayed depending on what they input

#Welcome----------------------------------------------------------------
def Welcome():
    #This function will display welcome message
    print('\nThis program will calculate total passing yards \n')
    print('----------------------------------------------------')

#Get user inputs for passing yards until they stop entering-------------
def GetPassingYards():
    #This function will prompt for yards input and calculate/display total yards
    sum = 0 #initialize the sum to start at 0
    
    total = int(input('\nInput passing yards (hit 0 when finished): \n')) #prompt user for yards, and the sentinel '0' when finished
    while (total != 0):  #created a while loop so long as input is not equal to 0
        sum = sum + total  #add together the inputs
        total = int(input('\nInput passing yards (hit 0 when finished): \n')) #re-prompt the user for yards until they enter 0
    print('Total Yards: ',sum) #display the output

def main(): #call the functions to run the program
    Welcome()
    GetPassingYards()
   
    
main()
        
        
    


    
    
