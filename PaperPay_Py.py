#Python Code
#This program will calculate and display pay information for a paper route
#User will be prompted for number of papers delivered per day
#User will be prompted for number of days worked
#User will be prompted for their weekly tips

#Developer: Derrick Hobbs CMIS102  Date: 08/30/2022

def main():
    #Initialize variables
    paperPrice = 2.99   #using 2.99 as the cost of each newspaper
    rateComm = .25      #using a commission rate of 25% per paper

    #Display welcome message
    print("\nWelcome to your weekly pay calculation")
    print("\nLet's find out how much you made this week!")

    #Prompt user for number of papers delivered per day
    numPapers = int(input("\n How many deliveries are on your route? "))

    #Prompt user for number for days worked
    numDays = int(input("\n How many days did you work? "))

    #Prompt user for their tips received
    wkTips = float(input("\n How much did you receive in tips? "))

    #Calculate the total papers for the week
    totalPapers = numPapers * numDays

    #Calculate the weekly salary
    wkSal = (totalPapers * paperPrice) * rateComm

    #Calculate weekly total pay
    totalPay = wkSal + wkTips

    #Display total papers delivered
    #Display weekly salary
    #Display tips for the week
    #Display total pay for the week
    print("\nYou delivered", totalPapers,"newspapers\n")
    print("Since you made", wkSal,"in commission, and",wkTips,"in tips...\n")
    print("Your total pay for the week is", totalPay,"\n")

    #Execute-----------------------------------------------------------------
main()
    
    
    

    
                    
