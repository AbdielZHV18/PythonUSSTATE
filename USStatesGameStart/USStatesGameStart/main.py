import turtle 

import pandas as pd

import pytest

#Find the Item in the list
def find(mylist, name):
    try:
        mylist.index(name)
        return True
    except:
        return False;

#Input bool to control exit
is_searching = True

#import the information from the cvs file and makes the State the index
myList = pd.read_csv('50_states.csv', index_col=[0])


#List That Hold The States
foundStateList= []

#List that Hold found State
StateList = []

#Transfer all the States to the 
for state in myList.index:
    StateList.append(state)

print(StateList)

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

        #Check if the user input 
        if stateSearch == "Exit" or stateSearch == "exit" or stateSearch == "":
            
            #Turn off the flag
            is_searching = False

        #If the user input is a state
        else:

            for state in StateList:
                if state == stateSearch and find(foundStateList,stateSearch) == False:

                    #Add the state to the list
                    foundStateList.append(stateSearch)
                    
                    #Find the Index the State is in the state list
                    temp = StateList.index(stateSearch)

                    #Pops the State out of the List
                    StateList.pop(temp)

                    #gets the X position of the state
                    myX = myList.loc[stateSearch].values[0]
                    
                    #gets the Y position of the state
                    myY =myList.loc[stateSearch].values[1]

                    #Move to Appropiate Location
                    myMarker.goto(myX,myY)

                    StateTittle = turtle.Turtle()

                    StateTittle.color("green")
                    
                    StateTittle.penup()

                    StateTittle.hideturtle()

                    StateTittle.goto(myX,myY)

                    StateTittle.write(stateSearch,align= "center", font= ["Arial", 14, "normal"])

                    print(foundStateList)

    
    #if the user input is not found or invalid
    except KeyError:
        
        #Does nothing but looks cute there :)
        continue

#Hides the Marker
myMarker.hideturtle()

#Gets the amount of states that wasn't found
remainState = len(StateList)

#Show the amount of states
if remainState > 0:

    for state in StateList:

        #Create a Turtle that will 
        StateTittleLost = turtle.Turtle()

        #Changes the Speend of the Turtle
        StateTittleLost.speed(20)

        #Makes the Turtle Red
        StateTittleLost.color("red")

        #Makes the Turtle Pen Invisible
        StateTittleLost.penup()

        #Make the Head of the turtle Invisible
        StateTittleLost.hideturtle()

        #Gets the State Location
        lostStateX = myList.loc[state].values[0]
        lostStateY = myList.loc[state].values[1]

        #Moves the Turtle to the State Location
        StateTittleLost.goto(lostStateX,lostStateY)

        #Writes the Name of the State
        StateTittleLost.write(state, align="center", font=["Arial", 10, "normal"])

    myMarker.goto(0,200)

    myMarker.write(f"You lost by {remainState} states", align="center", font=["Arial", 20, "bold"])




#Keeps the program until it's closed
myScreen.mainloop()
