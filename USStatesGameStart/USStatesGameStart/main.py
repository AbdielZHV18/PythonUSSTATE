import turtle

import pandas as pd

#Input bool to control exit
is_searching = True

#import the information from the cvs file and makes the State the index
myList = pd.read_csv('50_states.csv', index_col=[0])

#Create Screen
myScreen = turtle.Screen()

# Create a Turtle Icon
myMarker = turtle.Turtle()

#Makes Untraceble
myMarker.penup()

#Make the Marker Bigger
myMarker.shapesize(2)

#Move to Appropiate Location
myMarker.goto(0,0)

#Adjustes the Screen Appereances
myScreen.setup(725,491)

#Set Background as the US Image
myScreen.bgpic("blank_states_img.gif")

while is_searching:
    #Prompt the user write the appropiate state
    stateSearch = turtle.textinput("State?","Which State do you wish to find?:")

    try:
        #Capitalizes the Word
        stateSearch = stateSearch.capitalize()

        #Check if the user input 
        if stateSearch == "Exit":
            
            #Turn off the flag
            is_searching = False

            #Terminates the Program
            myScreen.bye()

        #If the user input is a state
        else:
            #gets the X position of the state
            myX = myList.loc[stateSearch].values[0]

            #gets the Y position of the state
            myY =myList.loc[stateSearch].values[1]

            #Move to Appropiate Location
            myMarker.goto(myX,myY)
    
    #if the user input is not found or invalid
    except KeyError:
        
        #Does nothing but looks cute there :)
        continue

#Keeps the program until it's closed
myScreen.mainloop()