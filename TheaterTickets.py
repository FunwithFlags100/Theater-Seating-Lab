#Efren Aguirre CIS129 
#7/14/2021
#This program calculates the revenue of a theater based on the number of seats sold depending on which section they were located in

def main():
    startProgram = input('Do you want to start calculating your revenue? (Enter Yes or No)')
    startProgram = startProgram.lower()    #prime read variable to enter loop and set variable to lower case
    sectionOneSeats = 0
    sectionTwoSeats = 0
    sectionThreeSeats = 0
    
    while startProgram == 'yes':
        print('Which section tickets are you entering?')
        print('Option 1: section one tickets')
        print('Option 2: section two tickets')
        print('Option 3: section three tickets')
        option = int(input('Enter the option number:'))
        
        #input validation for the option number 
        while option != 1 and option != 2 and option != 3:
            print('Please enter one of the three valid inputs! (1,2,3)')
            option = int(input('Enter the option number:'))

        #decision structure that decides which option number was entered
        if option == 1:
            sectionOneSeats = getSectionOne(sectionOneSeats)
        elif option == 2:
            sectionTwoSeats = getSectionTwo(sectionTwoSeats) 
        elif option == 3:
            sectionThreeSeats = getSectionThree(sectionThreeSeats) 

        startProgram = input('Do you have more seats to enter? (Yes or No)')
        startProgram = startProgram.lower()
        
    totalRevenue = getRevenue(sectionOneSeats, sectionTwoSeats, sectionThreeSeats)

    print('Your total revenue is $', totalRevenue)


#Calculates the number of section one seats sold
def getSectionOne(sectionOneSeats):
    seatCounter = int(input('Enter how many seats in section one were sold:'))
    #input validation for the number of seats sold
    while seatCounter < 0 or seatCounter > 300:
        print('Please enter a valid number of seats, between 0 and 300.')
        seatCounter = int(input('Enter how many seats in section one were sold:'))

    sectionOneSeats = sectionOneSeats + seatCounter
    #input validation that prevents the user from exceeding maximum seat count
    while sectionOneSeats > 300:
        sectionOneSeats = sectionOneSeats - seatCounter
        print('You have exceed the maximum number of seats for this section!!!')
        print('The maximum number of seats in section one is 300.')
        print('The current seat count for section one is:', sectionOneSeats)
        seatCounter = int(input('Please enter a new value for number of section one seats sold that does not exceed the maximum number of section one seats:'))
        sectionOneSeats = sectionOneSeats + seatCounter
    return sectionOneSeats

#calculates the number of section two seats sold
def getSectionTwo(sectionTwoSeats):
    seatCounter = int(input('Enter how many seats in section two were sold:'))
    #input validation loop that checks the number of seats sold entered
    while seatCounter < 0 or seatCounter > 500:
        print('Please enter a valid number of seats, between 0 and 500.')
        seatCounter = int(input('Enter how many seats in section two were sold:'))

    sectionTwoSeats = sectionTwoSeats + seatCounter
 #input validation that prevents the user from exceeding maximum seat count
    while sectionTwoSeats > 500:
        sectionTwoSeats = sectionTwoSeats - seatCounter
        print('You have exceed the maximum number of seats for this section!!!')
        print('The maximum number of seats in section two is 500.')
        print('The current seat count for section Two is:', sectionTwoSeats)
        seatCounter = int(input('Please enter a new value for number of section two seats sold that does not exceed the maximum number of section Two seats:'))
        sectionTwoSeats = sectionTwoSeats + seatCounter
   
    return sectionTwoSeats

#calculates the number of section three seats sold
def getSectionThree(sectionThreeSeats):
    seatCounter = int(input('Enter how many seats where sold in section three:'))
    #input validation loop that checks the number of seats sold entered
    while seatCounter < 0 or seatCounter > 200:
        print('Please enter a valid number of seats, between 0 and 200.')
        seatCounter = int(input('Enter how many seats in section three were sold:'))

    sectionThreeSeats = sectionThreeSeats + seatCounter
  #input validation that prevents the user from exceeding maximum seat count  
    while sectionThreeSeats > 200:
        sectionThreeSeats = sectionThreeSeats - seatCounter
        print('You have exceed the maximum number of seats for this section!!!')
        print('The maximum number of seats in section Three is 200.')
        print('The current seat count for section Three is:', sectionThreeSeats)
        seatCounter = int(input('Please enter a new value for number of section three seats sold that does not exceed the maximum number of section three seats:'))
        sectionThreeSeats = sectionThreeSeats + seatCounter
    return sectionThreeSeats

#calculates the total revenue
def getRevenue(sectionOneSeats, sectionTwoSeats, sectionThreeSeats):
    total = (sectionOneSeats * 20) + (sectionTwoSeats * 15) + (sectionThreeSeats * 10)
    return total


main()
