#Name:  Derrick Hobbs
#Class: CMIS102 Week 4 Discussion
#Date:  9/11/2022


#This is a program that is used to estimate yearly or monthly retirement income
#First input = User will be prompted for their portfolio size
#Second input = User will be prompted for their preference monthly or yearly payout
#Output will be calculated and displayed depending on what they choose

#Welcome-----------------------------------------------------------------------
def Welcome():
    #This function will display the welcome message
    print('\n\nUse this estimator to plan your monthy, or yearly retirement income')
    print('--------------------------------------------------------------------')

#Get portfolio size-------------------------------------------------------------
def GetPortfolioInput():
    #This function will prompt user for their portfolio size and validates >0 and enough 
    #Input: none
    #Output: portSize

    portSize = -1
    count = 0

    #Prompt for portfolio size
    portSize = float(input('\nHow much have you saved for retirement? \n'))
    #Validate input
    if (portSize <= 0):
            print('\nPlease enter a positive number \n')
            portSize = float(input('\nHow much have you saved for retirement? \n'))
    elif (portSize < 100000):
            print('\nNot enough saved to generate income \n')
            portSize = float(input('\nHow much have you saved for retirement? \n'))
            
    return (portSize)

#Get the conversion inputs--------------------------------------------------------
def GetHowOftenInput():
    #This function prompts and validates the input for conversion choice
    #Input: none
    #Output: option chosen

    #Prompt user for monthly or yearly income
    print('\nWould you like a Monthly or Yearly income calculation? \n')
    print(' M for Monthly \n')
    print(' Y for Yearly \n')
    option = input()

    #Convert to uppercase and then check for not M and not Y
    if(option.upper() != 'M' and option.upper() != 'Y'):
       print('***Invalid***')
       

    return (option)
        
#Convert to Monthly income---------------------------------------------------------
def ConvMonthIncome(portfolio):
    #This function converts portfolio to monthly income
    #Input:  portfolio
    #Output: monthly income

    payPerMonth = (0.035 / 12)

    monthly_income = portfolio * payPerMonth

    return (monthly_income)

#Convert to Yearly income----------------------------------------------------------
def ConvYearIncome(portfolio):
    #This function converts portfolio to yearly income
    #Input: portfolio
    #Ouput: yearly income

    payPerYear = 0.035

    yearly_income = portfolio * payPerYear

    return (yearly_income)

#Main Program----------------------------------------------------------------------
def main():
    #Call welcome message
    Welcome()

    #Prompt for the portfolio size and validate
    portSize = GetPortfolioInput()

    if (portSize > 0):
        #Prompt for conversion choice and validate
        option = GetHowOftenInput()

        #Call conversion based on user input
        if (option.upper() == 'M'):
            #Call function to monthly income
            payPerMonth = round(ConvMonthIncome (portSize),2)
            print('\nYou could have',payPerMonth,'per month')

        elif (option.upper() == 'Y'):
            #Call function to yearly income
            payPerYear = round(ConvYearIncome (portSize),2)
            print('\nYou could have',payPerYear,'per year')

    else:
        print('***Invalid***')

    #Display exit message
    print('\nThank you for using this retirement income estimator')
        

    
            
    

    #execute---------------------------------------------------------------------------
main()
    
    
