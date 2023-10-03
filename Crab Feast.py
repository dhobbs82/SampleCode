#Name:  Derrick Hobbs
#Class: CMIS102 Week 3 Discussion
#Date:  9/5/2022


#This is a program that is used to calculate if you have enough crabs for your feast
#User will be prompted for the number of crabs
#User will be prompted for the size of crabs
#User will be prompted for how many people are attending
#Output will be  number of crabs per person whether and not they got enough for a feast, based on size and number of crabs each

def main():

    #display welcome message
    print('\nDid you get enough crabs for the feast?')
    print('Use this calculator based on how many crabs, people, and crab size(1=Lg 2=Med 3=Sm)')

    #prompt user for the number of crabs
    numCrabs = int(input('\nHow many crabs did you purchase? \n'))
    if numCrabs >= 1:
            print('Thats a good start! \n')
    elif numCrabs <= 0:
            print('Thats not gonna be enough! Input a number greater than 1 \n')
            numCrabs = int(input('\nHow many crabs did you purchase? \n'))
        
    #prompt user for the size of crabs
    sizeCrabs = int(input('\nWhat size crabs did you purchase(1/2/3)? \n'))
    if sizeCrabs == 3 or sizeCrabs == 2 or sizeCrabs == 1:
        print('Sounds great...! \n')
    else:
        print('Enter 1 for Large, 2 for Medium, or 3 for Small \n')
        sizeCrabs = int(input('\nWhat size crabs did you purchase(1/2/3)? \n'))
              
    #prompt user for the number of people attending
    numPeople = int(input('\nHow many people are attending? \n'))
    if numPeople > 1:
        print('Almost time to eat! \n')
    else:
        print('What? Enter a number greater than 1 \n')
        numPeople = int(input('\nHow many people are attending? \n'))
              
    #calculate how many crabs per person
    enoughCrabs = float(numCrabs/numPeople)

    #display output is that enough based on size
    if enoughCrabs - sizeCrabs >= 3:
        print('\n',enoughCrabs,'crabs each, that should be enough! \n')
    else:
        print('\n',enoughCrabs,'crabs each, thats not gonna be enough... \n')
            
    

    #execute---------------------------------------------------------------------------
main()
    
    
