#Name:  Derrick Hobbs
#Class: CMIS102 Week 7 Discussion
#Date:  10/2/2022


#This is a program that populates an empty array for variables: ages
#the variables are supplied by the user within a loop requiring 5 inputs
#performs a modification to each element of the array by adding 4 years
#displays the modified array
#displays the oldest





def main():
    agelist = get_input()
    agelist = modify_agelist(agelist)
    oldest(agelist)

#populate an array, 5 elements, within a loop supplied by user
def get_input():
    agelist = []
    ages = 0
    
    while (ages < 5):
        age = int(input("Enter the ages of you and your 4 best friends: "))   
        agelist.append(age)
        ages = ages + 1


    print("\nYour ages now are: ",agelist,"\n")

    return agelist

#modify each element of array using second loop    
def modify_agelist(agelist):

    for age in range(len(agelist)):
        agelist[age] = agelist[age] + 4

    return agelist
        
    

#display the modified array
def oldest(agelist):
        

    print("Your ages will be",agelist,"when the World Cup comes to America")
    print("\nThe oldest will be",max(agelist),"when the World Cup comes to America")

        


    
            
main()
