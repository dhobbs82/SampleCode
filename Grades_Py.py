#Python Code
#This program includes a list of four student names
#Each student has input for 3 grades(discussion,quiz,assignment)
#This program uses a function to compute the weighted average for each student
#The for loop calls the function successively, names the student, displays grade
#A check is made for highest grade, displays highest grade/student at the end

#Developer: Derrick Hobbs CMIS102  Date: 09/18/2022


#Call the main function------------------------------------

def main():
    #Initialize
    students = ('Larry', 'Moe', 'Curly', 'Shemp')
    highGrade = -100

    #Display Welcome Message
    Welcome()

    #Loop for the student's names
    for student in students:

        #get grades
        totalScore = GetTotalScore(student)

        #determine highest grade
        if (totalScore > highGrade):
            highGrade = totalScore     #save the grade
            highGradeStudent = student  #save the name

    #Call High Grade function
    DisplayHighGrade (highGrade, highGradeStudent)

#Functions--------------------------------------------------
def Welcome():
    print('\nWelcome to the grade book') #notice the \n is a new line
    print('This program will calculate the grades of four students')
    print('It will also determine who has the highest grade\n')

def GetTotalScore(student):

    totalGradesScore = 0
    
    #Display student and get each grade
    print('Please enter the grades for: \t', student)
     
    print('Enter the discussion grade: ')   #20% weighting discussion
    disGrade = float( input() )
    #Validate the grade is > 0
    if(disGrade < 0):
        print('Enter the discussion grade: ')
        disGrade = float( input() )
                
    #Validate the grade is > 0
    print('Enter the quiz grade: ')         #30% weighting quiz
    quizGrade = float( input() )
    if(quizGrade < 0):
        print('Enter the quiz grade: ')
        quizGrade = float( input() )
        
    #Validate the grade is > 0
    print('Enter the assignment grade: ')   #50% weighting assignment
    assGrade = float( input() )
    if(assGrade < 0):
        print('Enter the assignment grade: ')
        assGrade = float( input() )


    #calculate weighted grade by applying weights and totaling 
    totalGradesScore = totalGradesScore + ((disGrade*.2)+(quizGrade*.3)+(assGrade*.5))
    
    #display each student's grade
    print('Grade for',student,'is:\t\t',totalGradesScore,'\n\n')
    print('----------------------------------------------------------')

    return (totalGradesScore)
        

def DisplayHighGrade (highGrade, highGradeStudent):
    #Display the highest grade and the student with the highest grade
    print('\nThe student with the highest grade of',highGrade,'is',highGradeStudent)
    
    
    
#Execute----------------------------------------------------------------------------
main()
