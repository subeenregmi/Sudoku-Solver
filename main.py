import copy

def createSudokuBoard(filename):
	board = []
	file = None
	try: 
		file = open(filename, "r")
	except:
		print(f"File '{filename}' does not exist")
		return None
	
	for line in file:
		row = []
		for digit in line:
			if digit == '\n':
				continue
			row.append(int(digit))
		board.append(row)
			
	file.close()
	return board

def checkIfInvalidBoard(board):
	for i in range(9):
		current_row = set({})
		current_col = set({})
		for j in range(9):
			if (board[i][j] == 0) or (board[j][i] == 0):
				continue

			if board[i][j] in current_row:
				return False
			if board[j][i] in current_col:
				return False

			current_row.add(board[i][j])
			current_col.add(board[j][i])
	
	for i in range(3):
		for j in range(3):
			current_box = set()
			for x in range(3):
				for y in range(3):	
					if board[i*3 + x][j*3 + y] == 0:
						continue
					if board[i*3 + x][j*3 + y] in current_box:
						return False
					current_box.add(board[i*3 + x][j*3 + y])

	return True 

def solveSudoku(board):
	solved = False
	solvingb = copy.deepcopy(board)
	i = 0 
	j = 0 
	while not solved:
		solvingb[i][j] += 1
		if solvingb[i][j] >= 10:
			solvingb[i][j] = 0
			if j-1 < 0:
				
