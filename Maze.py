import msvcrt
import os


locationColumn = 1
locationLine = 2

#checks a players movement and either moves them, or doesnt if isCollision says no
def move(key):
	global locationColumn
	global locationLine
	global message
	message = ' '
	
########Player moves RIGHT
	if( 'd' == key ):
		
		#sets previous location to a ' '
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
	if( 'a' == key ):
		
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
	if( 'w' == key ):
		
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
	if( 's' == key ):
		
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


#the actual maze made of 8s and spaces
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


#Retrieves the proper list for the line we're on
lineGet = {1: line1, 2:line2, 3:line3, 4:line4, 5:line5, 6:line6, 7:line7, 8:line8, 9:line9, 10:line10, 11:line11, 12:line12, 13:line13, 14:line14, 15:line15, 16:line16, 17:line17, 18:line18, 19:line19}

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
	for x in range(1, 20):
		
		#temporarily stores the current list that was just joined as each was converted to a string
		temp =''.join(str(y) for y in lineGet[x] )
		
		#prints string with spaces inbetween each character
		print(" ".join(temp))
	
	print(message)
	
#opening message exmplaining game
print('Use WASD to navigate the maze')
print('You start in the top left corner')
print('Hit enter twice when ready')
msvcrt.getch()

#loops everything until player reaches the bottom of the maze
while(locationLine != 19):
	playerInput("")
	printMaze()

#once theyve excaped the loop/maze
print('YOU WON!')
msvcrt.getch()

