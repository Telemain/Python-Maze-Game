from random import shuffle, randrange

def make_maze(w = 16, h = 8):

	#keeps track of where has been visited
	#makes a series of lists forming a box with the right and bottom as 1s, everything else as 0s
	vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]


	#creates a "solid" row for each of these depending on the height
	#(adds and extra "hor" for the bottomest row)
	ver = [["|  "] * w + ['|'] for i in range(h)] + [[]] #idk what this blank does but it allows the hor to place after it
	hor = [["+--"] * w + ['+'] for i in range(h + 1)]

	def walk(x, y):
		vis[y][x] = 1
		#print(vis)

		#lists the 4 neighbors, then shuffles them
		d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
		shuffle(d)

		#loops through those 4 neighbors
		for (xx, yy) in d:
			#if visited, skip to next neighbor
			if vis[yy][xx]:
				#print(vis)
				continue
			#if horizontal, replace the "+--" with a "+	 "
			if xx == x:
				hor[max(y, yy)][x] = "+  "
			#if vertical, replace the " | " with a "   "
			if yy == y:
				print(x)
				print(xx)
				ver[y][max(x, xx)] = "   "
			#then repeat for the neighbor
			walk(xx, yy)

	#starts the walk at a random location
	walk(randrange(w), randrange(h))

	s = ""

	#takes first entry in hor and ver and joins them, then the same for the next set. Then it sets it to s
	for (a, b) in zip(hor, ver):
		s += ''.join(a + ['\n'] + b + ['\n'])
	return s

if __name__ == '__main__':
	print(make_maze())