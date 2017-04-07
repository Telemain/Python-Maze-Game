import msvcrt
import os
from random import shuffle, randrange

os.system('mode con: cols=90 lines=45')

locationColumn = 1
locationLine = 2
difficult = 'n'

#checks a players movement and either moves them, or doesnt if isCollision says no
def move(key):
	global locationColumn
	global locationLine
	global message
	message = ' '

####Player moves RIGHT
	if( b'd' == key ):

		#sets previous location to a ' '
		#DOES NOT SET NEW LOCATION, PRINT SCREEN
		temp2 = lineGet[locationLine]
		temp2[locationColumn] = ' '

		locationColumn = locationColumn + 1

		#Player hits wall
		if( True == isCollision(locationColumn, locationLine) ):
			locationColumn = locationColumn - 1
			message = 'There is a wall there!'
		#Player just moves
		else:
			message = 'You move right one'

####Player moves LEFT
	if( b'a' == key ):

		#sets previous location to a ' '
		temp2 = lineGet[locationLine]
		temp2[locationColumn] = ' '

		locationColumn = locationColumn - 1

		#Player hits wall
		if( True == isCollision(locationColumn, locationLine) ):
			locationColumn = locationColumn + 1
			message = 'There is a wall there!'

		#Player just moves
		else:
			message = 'You move left one'

####Player moves UP
	if( b'w' == key ):

		#sets previous location to a ' '
		temp2 = lineGet[locationLine]
		temp2[locationColumn] = ' '

		locationLine = locationLine - 1

		#Player hits wall
		if( True == isCollision(locationColumn, locationLine) ):
			locationLine = locationLine + 1
			message = 'There is a wall there!'

		#Player just moves
		else:
			message = 'You move up one'

####Player moves DOWN
	if( b's' == key ):

		#sets previous location to a ' '
		temp2 = lineGet[locationLine]
		temp2[locationColumn] = ' '

		locationLine = locationLine + 1

		#Player hits wall
		if( True == isCollision(locationColumn, locationLine) ):
			locationLine = locationLine - 1
			message = 'There is a wall there!'

		#Player just moves
		else:
			message = 'You move down one'


#checks if there is a 'wall' at the current coordinates
def isCollision(column, line):

	#gets character at location
	currentLine = lineGet[line]

	#compares said character to an 8
	if( 8 == currentLine[column]):
		return True
	else:
		return False


#returns the variable name for the line based upon the line number. ie returns line4 if you give it 4
def lineAssignments():
	global lineGet
	lineGet = {1: line1, 2:line2, 3:line3, 4:line4, 5:line5, 6:line6, 7:line7, 8:line8, 9:line9, 10:line10, 11:line11, 12:line12, 13:line13, 14:line14, 15:line15, 16:line16, 17:line17, 18:line18, 19:line19, 20:line20, 21:line21, 22:line22, 23: line23, 24:line24, 25:line25, 26:line26, 27:line27, 28:line28, 29:line29, 30:line30, 31:line31, 32:line32, 33:line33, 34:line34, 35:line35, 36:line36, 37:line37, 38:line38, 39:line39, 40:line40, 41:line41}
	print('lineassignmentsuccess')

	
#gets the players input and passes it on to the move function
def playerInput(self):
	keyPress = msvcrt.getch()
	move(keyPress)

	
#prints the maze
def printMaze():
	#clears the screen
	os.system('cls')

	#sets current location to an X
	temp2 = lineGet[locationLine]
	temp2[locationColumn] = 'X'

	#loops through all the rows
	for x in range(1, finalLine + 1):

		#temporarily stores the current list that was just joined as each was converted to a string
		temp =''.join(str(y) for y in lineGet[x] )

		#prints string with spaces inbetween each character
		print(" ".join(temp))

	print(message)

###############################################################################################################################################################################################################################################################################################

#opening message exmplaining game
print('Use WASD to navigate the maze')
print('You start in the top left corner, exit is in the bottom right corner.')
difficult = input('Do you want the more difficult maze? (y/n)')

#the actual maze made of 8s and spaces
#2 different versions
#mazes are in line format so they can be fairly easily edited and displayed
if( 'y' == difficult ):
	finalLine = 41

	line1 = [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]
	line2 = [8,' ',8,' ',' ',' ',8,' ',8,' ',' ',' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',8,' ',' ',' ',' ',' ',8]
	line3 = [8,' ',8,8,8,' ',8,' ',8,' ',8,' ',8,8,8,8,8,' ',8,8,8,' ',8,' ',8,' ',8,8,8,8,8,8,8,' ',8,' ',8,8,8,' ',8]
	line4 = [8,' ',' ',' ',8,' ',' ',' ',' ',' ',8,' ',8,' ',8,' ',8,' ',8,' ',' ',' ',8,' ',8,' ',8,' ',' ',' ',' ',' ',8,' ',8,' ',' ',' ',8,' ',8]
	line5 = [8,8,8,' ',8,' ',8,' ',8,8,8,' ',8,' ',8,' ',8,' ',8,' ',8,8,8,' ',8,' ',8,' ',8,' ',8,' ',8,8,8,8,8,' ',8,8,8]
	line6 = [8,' ',8,' ',8,' ',8,' ',8,' ',8,' ',' ',' ',' ',' ',8,' ',' ',' ',' ',' ',8,' ',8,' ',' ',' ',8,' ',8,' ',' ',' ',8,' ',' ',' ',' ',' ',8]
	line7 = [8,' ',8,' ',8,' ',8,8,8,' ',8,' ',8,8,8,' ',8,' ',8,' ',8,' ',8,' ',8,8,8,8,8,8,8,8,8,' ',8,' ',8,8,8,' ',8]
	line8 = [8,' ',' ',' ',8,' ',8,' ',' ',' ',8,' ',8,' ',8,' ',' ',' ',8,' ',8,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',8,' ',8,' ',8,' ',8,' ',8]
	line9 = [8,' ',8,8,8,' ',8,' ',8,8,8,8,8,' ',8,8,8,8,8,8,8,8,8,8,8,' ',8,8,8,8,8,8,8,8,8,' ',8,' ',8,' ',8]
	line10 = [8,' ',8,' ',8,' ',' ',' ',' ',' ',' ',' ',8,' ',8,' ',' ',' ',' ',' ',' ',' ',' ',' ',8,' ',' ',' ',' ',' ',8,' ',' ',' ',8,' ',8,' ',8,' ',8]
	line11 = [8,' ',8,' ',8,' ',8,' ',8,' ',8,8,8,' ',8,' ',8,8,8,8,8,8,8,8,8,' ',8,' ',8,8,8,' ',8,' ',8,8,8,' ',8,' ',8]
	line12 = [8,' ',8,' ',8,' ',8,' ',8,' ',8,' ',' ',' ',' ',' ',8,' ',' ',' ',' ',' ',8,' ',8,' ',8,' ',' ',' ',' ',' ',8,' ',' ',' ',' ',' ',' ',' ',8]
	line13 = [8,' ',8,' ',8,' ',8,8,8,' ',8,' ',8,' ',8,' ',8,' ',8,8,8,' ',8,' ',8,' ',8,8,8,8,8,8,8,' ',8,8,8,' ',8,8,8]
	line14 = [8,' ',' ',' ',' ',' ',' ',' ',8,' ',' ',' ',8,' ',8,' ',8,' ',' ',' ',8,' ',' ',' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',8,' ',8]
	line15 = [8,' ',8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,' ',8,8,8,8,8,8,8,' ',8,8,8,8,8,8,8,8,8,8,8,' ',8]
	line16 = [8,' ',' ',' ',8,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',8,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',8,' ',' ',' ',8]
	line17 = [8,8,8,' ',8,' ',8,8,8,8,8,8,8,' ',8,8,8,8,8,8,8,' ',8,8,8,' ',8,8,8,' ',8,8,8,' ',8,8,8,8,8,' ',8]
	line18 = [8,' ',' ',' ',' ',' ',' ',' ',' ',' ',8,' ',' ',' ',' ',' ',8,' ',8,' ',' ',' ',8,' ',' ',' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',' ',' ',' ',' ',8]
	line19 = [8,' ',8,' ',8,8,8,8,8,8,8,' ',8,8,8,8,8,' ',8,8,8,8,8,' ',8,8,8,8,8,8,8,' ',8,8,8,8,8,8,8,8,8]
	line20 = [8,' ',8,' ',' ',' ',' ',' ',8,' ',8,' ',' ',' ',8,' ',' ',' ',' ',' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',' ',' ',8]
	line21 = [8,' ',8,8,8,' ',8,8,8,' ',8,8,8,8,8,' ',8,8,8,' ',8,8,8,' ',8,8,8,' ',8,8,8,8,8,' ',8,8,8,' ',8,' ',8]
	line22 = [8,' ',' ',' ',8,' ',' ',' ',' ',' ',' ',' ',8,' ',8,' ',8,' ',8,' ',' ',' ',' ',' ',' ',' ',8,' ',8,' ',' ',' ',8,' ',' ',' ',' ',' ',8,' ',8]
	line23 = [8,' ',8,8,8,8,8,8,8,' ',8,8,8,' ',8,8,8,' ',8,8,8,' ',8,8,8,8,8,' ',8,' ',8,' ',8,8,8,8,8,8,8,' ',8]
	line24 = [8,' ',' ',' ',' ',' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',8,' ',8,' ',' ',' ',' ',' ',8,' ',8,' ',' ',' ',' ',' ',' ',' ',' ',' ',8]
	line25 = [8,' ',8,8,8,8,8,' ',8,' ',8,' ',8,8,8,' ',8,8,8,' ',8,8,8,8,8,' ',8,8,8,8,8,8,8,8,8,8,8,8,8,' ',8]
	line26 = [8,' ',' ',' ',8,' ',8,' ',8,' ',8,' ',8,' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',' ',' ',8,' ',' ',' ',' ',' ',8,' ',' ',' ',' ',' ',8,' ',8]
	line27 = [8,' ',8,' ',8,' ',8,' ',8,' ',8,8,8,8,8,' ',8,' ',8,8,8,' ',8,8,8,8,8,' ',8,' ',8,8,8,' ',8,8,8,' ',8,' ',8]
	line28 = [8,' ',8,' ',8,' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',8,' ',8,' ',' ',' ',8,' ',' ',' ',' ',' ',8,' ',' ',' ',' ',' ',8,' ',8,' ',8,' ',8]
	line29 = [8,8,8,' ',8,' ',8,8,8,8,8,' ',8,' ',8,' ',8,' ',8,' ',8,8,8,' ',8,8,8,' ',8,8,8,8,8,8,8,' ',8,' ',8,' ',8]
	line30 = [8,' ',' ',' ',8,' ',' ',' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',' ',' ',' ',' ',8,' ',8,' ',' ',' ',' ',' ',' ',' ',8,' ',8,' ',8,' ',8,' ',8]
	line31 = [8,8,8,' ',8,8,8,' ',8,' ',8,8,8,8,8,' ',8,' ',8,' ',8,8,8,' ',8,8,8,8,8,8,8,8,8,' ',8,' ',8,' ',8,8,8]
	line32 = [8,' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',8,' ',8,' ',8,' ',8,' ',' ',' ',' ',' ',8,' ',8,' ',' ',' ',8,' ',' ',' ',8,' ',8,' ',' ',' ',8]
	line33 = [8,' ',8,8,8,8,8,8,8,8,8,8,8,' ',8,' ',8,8,8,8,8,8,8,8,8,' ',8,' ',8,' ',8,8,8,' ',8,' ',8,8,8,' ',8]
	line34 = [8,' ',' ',' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',8,' ',8,' ',' ',' ',' ',' ',8,' ',8,' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',' ',' ',' ',' ',8]
	line35 = [8,' ',8,8,8,' ',8,8,8,' ',8,' ',8,8,8,' ',8,' ',8,8,8,' ',8,' ',8,8,8,' ',8,8,8,' ',8,8,8,8,8,8,8,8,8]
	line36 = [8,' ',8,' ',8,' ',' ',' ',8,' ',8,' ',' ',' ',' ',' ',8,' ',8,' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',8,' ',8,' ',' ',' ',' ',' ',' ',' ',8]
	line37 = [8,' ',8,' ',8,' ',8,' ',8,' ',8,' ',8,8,8,8,8,' ',8,' ',8,8,8,8,8,' ',8,8,8,' ',8,' ',8,' ',8,8,8,' ',8,8,8]
	line38 = [8,' ',' ',' ',8,' ',8,' ',' ',' ',8,' ',' ',' ',' ',' ',' ',' ',8,' ',8,' ',' ',' ',8,' ',' ',' ',' ',' ',8,' ',8,' ',' ',' ',8,' ',8,' ',8]
	line39 = [8,' ',8,8,8,' ',8,8,8,' ',8,' ',8,8,8,8,8,8,8,' ',8,' ',8,' ',8,' ',8,8,8,' ',8,8,8,8,8,' ',8,' ',8,' ',8]
	line40 = [8,' ',' ',' ',8,' ',8,' ',' ',' ',8,' ',' ',' ',' ',' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',' ',' ',' ',' ',' ',' ',8,' ',' ',' ',8]
	line41 = [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,' ',8]
	print('Large maze success')
else:
	finalLine = 19

	line1  = [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]
	line2  = [8,' ',' ',' ',' ',' ',' ',' ',' ',8,' ',' ',' ',' ',' ',' ',8,' ',8]
	line3  = [8,' ',8,8,8,8,' ',8,' ',8,' ',8,8,8,8,' ',8,' ',8]
	line4  = [8,' ',8,' ',' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',' ',8,' ',8]
	line5  = [8,' ',8,' ',8,8,' ',8,8,8,' ',8,8,8,8,8,8,' ',8]
	line6  = [8,' ',8,' ',' ',8,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',8]
	line7  = [8,' ',8,8,8,8,8,8,8,8,8,8,8,' ',8,' ',8,8,8]
	line8  = [8,' ',' ',' ',' ',' ',' ',' ',' ',8,' ',' ',' ',' ',8,' ',8,' ',8]
	line9  = [8,8,8,8,8,8,' ',8,' ',8,' ',8,8,8,8,' ',8,' ',8]
	line10 = [8,' ',' ',' ',' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',' ',' ',' ',8]
	line11 = [8,' ',8,8,8,8,8,8,8,8,8,8,' ',8,8,8,8,8,8]
	line12 = [8,' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',' ',' ',' ',' ',' ',' ',8]
	line13 = [8,' ',8,' ',8,' ',8,8,8,' ',8,8,8,8,8,8,8,8,8]
	line14 = [8,' ',8,' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',' ',' ',' ',' ',8]
	line15 = [8,8,8,8,8,8,8,8,8,' ',8,' ',8,8,8,8,8,' ',8]
	line16 = [8,' ',' ',' ',' ',8,' ',' ',' ',' ',8,' ',8,' ',' ',' ',' ',' ',8]
	line17 = [8,8,' ',8,8,8,' ',8,8,' ',8,8,8,' ',8,8,8,8,8]
	line18 = [8,' ',' ',' ',' ',' ',' ',' ',8,' ',' ',' ',' ',' ',' ',' ',' ',' ',8]
	line19 = [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,' ',8]
	line20 = [8,' ',8,' ',' ',' ',' ',' ',8,' ',8,' ',' ',' ',8,' ',' ',' ',' ',' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',8,' ',' ',' ',' ',' ',8]
	line21 = []
	line22 = []
	line23 = []
	line24 = []
	line25 = []
	line26 = []
	line27 = []
	line28 = []
	line29 = []
	line30 = []
	line31 = []
	line32 = []
	line33 = []
	line34 = []
	line35 = []
	line36 = []
	line37 = []
	line38 = []
	line39 = []
	line40 = []
	line41 = []
	print('Small maze success')


#Retrieves the proper list for the line we're on
lineAssignments()

#loops everything until player reaches the bottom of the maze
while(locationLine != finalLine):
	playerInput("")
	printMaze()

#once theyve excaped the loop/maze
print('YOU WON!')
msvcrt.getch()

