#!/usr/bin/env python2

# CHALLENGE PROBLEM: 
#
# Use your check_sudoku function as the basis for solve_sudoku(): a
# function that takes a partially-completed Sudoku grid and replaces
# each 0 cell with an integer in the range 1..9 in such a way that the
# final grid is valid.
#
# There are many ways to cleverly solve a partially-completed Sudoku
# puzzle, but a brute-force recursive solution with backtracking is a
# perfectly good option. The solver should return None for broken
# input, False for inputs that have no valid solutions, and a valid
# 9x9 Sudoku grid containing no 0 elements otherwise. In general, a
# partially-completed Sudoku grid does not have a unique solution. You
# should just return some member of the set of solutions.
#
# A solve_sudoku() in this style can be implemented in about 16 lines
# without making any particular effort to write concise code.

# solve_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return valid unchanged
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return a 
# sudoku grid which passes a 
# sudoku checker. There may be
# multiple correct grids which 
# can be made from this starting 
# grid.   2,9,0,3,0,6,8,0,0
easy = [[2,9,1,0,0,0,0,7,0],
        [3,5,6,0,0,8,4,0,0],
        [8,7,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# Note: this may timeout 
# in the Udacity IDE! Try running 
# it locally if you'd like to test 
# your solution with it.
# 
# hard = [[1,0,0,0,0,7,0,9,0],
#         [0,3,0,0,2,0,0,0,8],
#         [0,0,9,6,0,0,5,0,0],
#         [0,0,5,3,0,0,9,0,0],
#         [0,1,0,0,8,0,0,0,2],
#         [6,0,0,0,0,4,0,0,0],
#         [3,0,0,0,0,0,0,1,0],
#         [0,4,0,0,0,0,0,0,7],
#         [0,0,7,0,0,0,3,0,0]]

def solve_sudoku (grid):
	space = search_least(grid)
	missing = get_missing(grid, space)
	check_solve(grid, space, missing)
	pass

def search_least(grid):
	zeros_horz = []
	zeros_vert = []
	zeros_sqr = []
	
	for i in range(9):
		zeros_horz.append(grid[i].count(0))
	myList = []
	for i in range(9):
		myLine = []
		for j in range(9):
			myLine.append(grid[j][i])
		myList.append(myLine)
	for i in range(9):
		zeros_vert.append(myList[i].count(0))
	def grab_block(x,y,m,n):
		myLine = []
		for i in range(m,n):
			for j in range(x,y):
				myLine.append(grid[j][i])
		return myLine
	myList = []
	myList.append(grab_block(0,3,0,3))		
	myList.append(grab_block(0,3,3,6))
	myList.append(grab_block(0,3,6,9))
	myList.append(grab_block(3,6,0,3))
	myList.append(grab_block(3,6,3,6))
	myList.append(grab_block(3,6,6,9))
	myList.append(grab_block(6,9,0,3))
	myList.append(grab_block(6,9,3,6))
	myList.append(grab_block(6,9,6,9))
	for i in range(9):
		zeros_sqr.append(myList[i].count(0))
		
	lowest = 9
	count = 0
	space = 0
	for i in range(9):
		count += 1
		if zeros_horz[i] < lowest:
			lowest = zeros_horz[i]
			space = count
	for i in range(9):
		count += 1
		if zeros_vert[i] < lowest:
			lowest = zeros_vert[i]
			space = count
	for i in range(9):
		count += 1
		if zeros_sqr[i] < lowest:
			lowest = zeros_sqr[i]
			space = count
	return space

def get_missing(grid, space):
	myList = []
	toRemove = []
	numCount = [1,2,3,4,5,6,7,8,9]
	if 1 <= space <= 9:
		space -= 1
		for i in range(9):
			print grid[space][i]
			if grid[space][i] in numCount:
				toRemove.append(grid[space][i])
		
	elif 10 <= space <= 18:
		space -= 10
		for i in range(9):
			print grid[i][space]
			if grid[i][space] in numCount:
				toRemove.append(grid[i][space])
		
	elif 19 <= space <= 27:
		def grab_block(x,y,m,n):
			myLine = []
			for i in range(m,n):
				for j in range(x,y):
					myLine.append(grid[i][j])
			return myLine
		space -= 19
		if space == 0: myList = grab_block(0,3,0,3)	
		elif space == 1: myList = grab_block(0,3,3,6)
		elif space == 2: myList = grab_block(0,3,6,9)
		elif space == 3: myList = grab_block(3,6,0,3)
		elif space == 4: myList = grab_block(3,6,3,6)
		elif space == 5: myList = grab_block(3,6,6,9)
		elif space == 6: myList = grab_block(6,9,0,3)
		elif space == 7: myList = grab_block(6,9,3,6)
		elif space == 8: myList = grab_block(6,9,6,9)
		for i in range(9):
			if myList[i] in numCount:
				toRemove.append(myList[i])
				
	for i in range(len(toRemove)):
		numCount.remove(toRemove[i])
	return numCount

def check_solve(grid, space, missing):
	pass

# look for square or line with least amount of open spaces
# get list of numbers missing
# start with lowest number
# see if any of the numbers have only one possibility, if one is successful then start that group over as things might have changed.
# start the whole process over

def check_sudoku(grid):
	if not check_size(grid):
		return None
	if not check_hor(grid):
		return False
	if not check_vert(grid):
		return False
	if not check_square(grid):
		return False
	return True

def check_size(grid):
    if len(grid) < 9 or len(grid) > 9:
		return None
    for i in range(len(grid)):
		if len(grid[i]) < 9 or len(grid[i]) > 9:
			return None
    return True

def check_hor(grid):
	for i in range(9):
		for j in range(9):
			if grid[i].count(j+1) > 1:
				return False
	return True
	
def check_vert(grid):
	myList = []
	for i in range(9):
		myLine = []
		for j in range(9):
			myLine.append(grid[j][i])
		myList.append(myLine)
	for i in range(9):
		for j in range(9):
			if grid[i].count(j+1) > 1:
				return False
	return True
	
def check_square(grid):
	def grab_block(x,y,m,n):
		myLine = []
		for i in range(m,n):
			for j in range(x,y):
				myLine.append(grid[j][i])
		return myLine
	myList = []
	myList.append(grab_block(0,3,0,3))		
	myList.append(grab_block(0,3,3,6))
	myList.append(grab_block(0,3,6,9))
	myList.append(grab_block(3,6,0,3))
	myList.append(grab_block(3,6,3,6))
	myList.append(grab_block(3,6,6,9))
	myList.append(grab_block(6,9,0,3))
	myList.append(grab_block(6,9,3,6))
	myList.append(grab_block(6,9,6,9))
	if not check_hor(myList):
		return False
	if not check_vert(myList):
		return False
	return True
	
#check_sudoku(easy)
solve_sudoku(easy)
