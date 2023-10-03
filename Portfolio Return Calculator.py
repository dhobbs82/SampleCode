#This is a program that is used to calculate portfolio performance vs s&p 500 avg
#User will be prompted for their stock investment return
#User will be prompted for their bond investment return
#Output will be how much they underperformed or outperformed the 10 year s&p avg

def main():
    #initialize variables
    spAvg = 9.52

    #display welcome message
    print('\nHow have you done compared to the stock market?')
    print('Use this calculator to find out...')

    #prompt user for their stock return percentage
    stockReturn = float(input('\nWhat was the weighted percent return for your Stocks? \n'))
    #prompt user for their bond return percentage
    bondReturn = float(input('\nWhat was the weighted percent return for your Bonds? \n'))

    #calculate their total return
    totalReturn = (stockReturn + bondReturn)/2

    #display output
    print('\nYour total return was',totalReturn,'vs.', spAvg,'for the stock market')

    #execute---------------------------------------------------------------------------
main()
    
    
