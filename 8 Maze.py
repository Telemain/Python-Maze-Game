#https://stackoverflow.com/questions/27017164/python-maze-generator-explanation
#Taught me how to make mazes

import msvcrt
import os
from random import shuffle, randrange
import time

os.system('mode con: cols=150 lines=75')

locationColumn = 1
locationLine = 2
lineGet = {}

h = 30
w = 30

#declares the line variables so it doesnt get mad, 100 should be enough
line1 = []; line2 = []; line3 = []; line4 = []; line5 = []; line6 = []; line7 = []; line8 = []; line9 = []; line10 = []; line11 = []; line12 = []; line13 = []; line14 = []; line15 = []; line16 = []; line17 = []; line18 = []; line19 = []; line20 = []; line21 = []; line22 = []; line23 = []; line24 = []; line25 = []; line26 = []; line27 = []; line28 = []; line29 = []; line30 = []; line31 = []; line32 = []; line33 = []; line34 = []; line35 = []; line36 = []; line37 = []; line38 = []; line39 = []; line40 = []; line41 = []; line42 = []; line43 = []; line44 = []; line45 = []; line46 = []; line47 = []; line48 = []; line49 = []; line50 = []; line51 = []; line52 = []; line53 = []; line54 = []; line55 = []; line56 = []; line57 = []; line58 = []; line59 = []; line60 = []; line61 = []; line62 = []; line63 = []; line64 = []; line65 = []; line66 = []; line67 = []; line68 = []; line69 = []; line70 = []; line71 = []; line72 = []; line73 = []; line74 = []; line75 = []; line76 = []; line77 = []; line78 = []; line79 = []; line80 = []; line81 = []; line82 = []; line83 = []; line84 = []; line85 = []; line86 = []; line87 = []; line88 = []; line89 = []; line90 = []; line91 = []; line92 = []; line93 = []; line94 = []; line95 = []; line96 = []; line97 = []; line98 = []; line99 = []; line100 = []


#now we make a list so we can call varying variable names
#(so we can use a variable in a variablename such as lineGet[i])
def lineAssignments():
	global lineGet
	lineGet = {1: line1, 2:line2, 3:line3, 4:line4, 5:line5, 6:line6, 7:line7, 8:line8, 9:line9, 10:line10, 11:line11, 12:line12, 13:line13, 14:line14, 15:line15, 16:line16, 17: line17, 18: line18, 19: line19, 20: line20, 21: line21, 22: line22, 23: line23, 24: line24, 25: line25, 26: line26, 27: line27, 28: line28, 29: line29, 30: line30, 31: line31, 32: line32, 33: line33, 34: line34, 35: line35, 36: line36, 37: line37, 38: line38, 39: line39, 40: line40, 41: line41, 42: line42, 43: line43, 44: line44, 45: line45, 46: line46, 47: line47, 48: line48, 49: line49, 50: line50, 51: line51, 52: line52, 53: line53, 54: line54, 55: line55, 56: line56, 57: line57, 58: line58, 59: line59, 60: line60, 61: line61, 62: line62, 63: line63, 64: line64, 65: line65, 66: line66, 67: line67, 68: line68, 69: line69, 70: line70, 71: line71, 72: line72, 73: line73, 74: line74, 75: line75, 76: line76, 77: line77, 78: line78, 79: line79, 80: line80, 81: line81, 82: line82, 83: line83, 84: line84, 85: line85, 86: line86, 87: line87, 88: line88, 89: line89, 90: line90, 91: line91, 92: line92, 93: line93, 94: line94, 95: line95, 96: line96, 97: line97, 98: line98, 99: line99, 100: line100}


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
		pMove = lineGet[locationLine]
		pMove[locationColumn] = ' '

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
		pMove = lineGet[locationLine]
		pMove[locationColumn] = ' '

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
		pMove = lineGet[locationLine]
		pMove[locationColumn] = ' '

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
		pMove = lineGet[locationLine]
		pMove[locationColumn] = ' '

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
	lineGet = {1: line1, 2:line2, 3:line3, 4:line4, 5:line5, 6:line6, 7:line7, 8:line8, 9:line9, 10:line10, 11:line11, 12:line12, 13:line13, 14:line14, 15:line15, 16:line16, 17:line17, 18:line18, 19:line19, 20:line20, 21:line21, 22:line22, 23: line23, 24:line24, 25:line25, 26:line26, 27:line27, 28:line28, 29:line29, 30:line30, 31:line31, 32:line32, 33:line33, 34:line34, 35:line35, 36:line36, 37:line37, 38:line38, 39:line39, 40:line40, 41:line41}

lineAssignments()

#gets the players input and passes it on to the move function
def playerInput(self):
	keyPress = msvcrt.getch()
	move(keyPress)


#prints the maze
def printMaze():

	#clears the screen
	os.system('cls')
	
	#sets current location to an X
	setX = lineGet[locationLine]
	setX[locationColumn] = 'X'

	#loops through all the rows
	for x in range(1, finalLine + 1):

		#temporarily stores the current list that was just joined as each was converted to a string
		linePrint =''.join(str(y) for y in lineGet[x] )

		#prints string with spaces inbetween each character
		print(" ".join(linePrint))

	print(message)


def generateMaze():

	#creates the two lists that make up alternating rows
	hor = [8, 8] * w + [8]
	ver = [8, " "] * w + [8]
	
	global lineGet
	
	lineGet[1] = hor

	#loops through the lines setting alternating rows to hor and ver and repeat
	#THE LIST() IS IMPORTANT, IT STOPS ALL THE LINES FROM BEING CHANGED TOGETHER
	for i in range(2, finalLine, 2):
		lineGet[i] = list(ver)
		i += 1
		lineGet[i] = list(hor)

	#adds a visual indicator for the exit
	lineGet[finalLine][w*2-1] = " "

	#creates a box of 0s surrounded by 1s to tell the wall breaking snake to stop
	#for it has hit a wall or hit itself
				#top--------- 	#left   #middle  #right	 #times height		#bottom------
	wallStay = [[1] * (w + 2)] + [[1] + [0] * w +  [1]  for _ in range(h)] + [[1] * (w + 2)]


	def makePaths(x, y):

		#sets the current location to a 1 on the wallStay array to mark that we've been here
		wallStay[y][x] = 1

		direction = [1, 2, 3, 4]
		shuffle(direction)

		#loops through the four cardinal directions (which have been randomly sorted)
		for d in direction:

			locationLine = y * 2
			locationColumn = x * 2 - 1

		#####Maze moves RIGHT
			if( 1 == d ):

				#checks if we've been here before or if it's the edge
				x += 1
				if( wallStay[y][x] ):

					x -= 1
					continue

				else:

					#sets location one to the right to a blank
					wallBreak = lineGet[locationLine]

					locationColumn = locationColumn + 1
					wallBreak[locationColumn] = ' '

					#continues down the rabbit hole
					makePaths(x, y)

		#####Maze moves LEFT
			elif( 2 == d ):

				#checks if we've been here before or if it's the edge
				x -= 1
				if( wallStay[y][x] ):

					x += 1
					continue

				else:

					#sets location one to the right to a blank
					wallBreak = lineGet[locationLine]

					locationColumn = locationColumn - 1
					wallBreak[locationColumn] = ' '

					#continues down the rabbit hole
					makePaths(x, y)

		#####Maze moves UP
			elif( 3 == d ):

				#checks if we've been here before or if it's the edge
				y -= 1
				if( wallStay[y][x] ):

					y += 1
					continue

				else:

					#sets location one to the up to a blank
					locationLine = locationLine - 1

					wallBreak = lineGet[locationLine]
					wallBreak[locationColumn] = ' '

					#continues down the rabbit hole
					makePaths(x, y)

		#####Maze moves DOWN
			elif( 4 == d ):

				#checks if we've been here before or if it's the edge
				y += 1
				if( wallStay[y][x] ):

					y -= 1
					continue

				else:

					#sets location one to the down to a blank
					locationLine = locationLine + 1

					wallBreak = lineGet[locationLine]
					wallBreak[locationColumn] = ' '

					#continues down the rabbit hole
					makePaths(x, y)

	
	#runs the above function to clear away walls
	#the math is to keep it away from the walls no matter the size
	if( 2 >= w ):
		makePaths(1, 1)
	else:
		makePaths(randrange(w-2)+1, randrange(h-2)+1)


######################################################################################################################################################################################################################################################

#opening message exmplaining game
print('Use WASD to navigate the maze')
print('You start in the top left corner, exit is in the bottom right corner.')

print("Dimensions greater than 10 are not recommended unless you have a huge screen and larger than 20 will break it")
print("The max size for a 1600X900 screen is 49 by 24")
w = eval(input('Enter the width: '))
h = eval(input('Enter the height: '))


#sets win condition
finalLine = (h * 2) + 1

generateMaze()
lineAssignments()
timeStart = time.time()

#loops everything until player reaches the bottom of the maze
while(locationLine != finalLine):
	playerInput("")
	printMaze()

#once theyve excaped the loop/maze
timeEnd = time.time()
print('YOU WON!')
print('And it only took you', timeEnd - timeStart, 'seconds')
wait = input()

