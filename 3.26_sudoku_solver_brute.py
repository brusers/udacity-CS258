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
#~ valid = [[5,3,4,6,7,8,9,1,2],
         #~ [6,7,2,1,9,5,3,4,8],
         #~ [1,9,8,3,4,2,5,6,7],
         #~ [8,5,9,7,6,1,4,2,3],
         #~ [4,2,6,8,5,3,7,9,1],
         #~ [7,1,3,9,2,4,8,5,6],
         #~ [9,6,1,5,3,7,2,8,4],
         #~ [2,8,7,4,1,9,6,3,5],
         #~ [3,4,5,2,8,6,1,7,9]]

valid = [[0,3,4,0,0,8,9,1,0],
         [6,7,2,0,9,5,3,0,8],
         [1,0,0,3,0,2,5,6,7],
         [0,5,9,7,0,0,4,2,3],
         [0,2,0,0,0,3,7,9,1],
         [7,1,0,9,2,4,8,5,0],
         [9,0,0,5,3,7,0,8,4],
         [2,0,7,4,1,9,6,3,5],
         [0,4,5,2,0,6,0,7,0]]
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
# grid.
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
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


import random
from copy import deepcopy

def solve_sudoku(grid):
	if check_sudoku(grid) == True:
		missing = search_missing(grid)						#when doing missing search, search each block and number 1-9
		while True:
			puzzle = deepcopy(grid)
			num_shuffle(missing)
			fill_spaces(puzzle, missing)
			if check_sudoku(puzzle):
				return puzzle
				break
	else:
		return check_sudoku(grid)

def num_shuffle(missing):
	for i in range(9):
		random.shuffle(missing[i][1])
			
def search_missing(grid):
	missing = [[1,[0]],[2,[0]],[3,[0]],[4,[0]],[5,[0]],[6,[0]],[7,[0]],[8,[0]],[9,[0]]]
	def grab_block(x,y,m,n):
		myLine = []
		num = []
		for i in range(m,n):
			for j in range(x,y):
				myLine.append(grid[i][j])
		for i in range(9):
			if i+1 not in myLine:
				num.append(i+1)
		return num
	missing[0][1] = (grab_block(0,3,0,3))		
	missing[1][1] = (grab_block(0,3,3,6))
	missing[2][1] = (grab_block(0,3,6,9))
	missing[3][1] = (grab_block(3,6,0,3))
	missing[4][1] = (grab_block(3,6,3,6))
	missing[5][1] = (grab_block(3,6,6,9))
	missing[6][1] = (grab_block(6,9,0,3))
	missing[7][1] = (grab_block(6,9,3,6))
	missing[8][1] = (grab_block(6,9,6,9))
	return missing

def fill_spaces(puzzle, missing):
	def fill_block(x,y,m,n,block):
		missNum = deepcopy(missing[block-1][1])
		for i in range(m,n):
			for j in range(x,y):
				if puzzle[i][j] == 0:
					puzzle[i][j] = missNum.pop()
	fill_block(0,3,0,3,1)
	fill_block(0,3,3,6,2)
	fill_block(0,3,6,9,3)
	fill_block(3,6,0,3,4)
	fill_block(3,6,3,6,5)
	fill_block(3,6,6,9,6)
	fill_block(6,9,0,3,7)
	fill_block(6,9,3,6,8)
	fill_block(6,9,6,9,9)

# seach for missing numers, including multiples if the exist -> [1,2,1,8,7,9,1,2,6]
# randomize the order of the missing numbers
# fill spaces in puzzle and test
# if fails, re-randomize order of missing numbers and try again until it passes

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
print solve_sudoku(easy)
